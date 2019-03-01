#-*-coding:utf-8-*-
import unittest
from pageobject.work import Work
from selenium import webdriver
from appium import webdriver
from framework.app_config import Config

class Get_Appnames(unittest.TestCase):
    '''
    功能描述:获取工作页面所有应用的名称
    '''
    # setUp（）方法用于测试用例执行前的初始化工作。如测试用例需要访问数据库，可以在setUp中建立数据库链接
    # 并进行初始化。如测试用例需要启动appium服务，则需要在该方法内启动appium服务
    @classmethod
    def setUp(self):
        '''
        测试前的准备工作
        :return:
        '''
        config = Config()
        self.driver = config.desired_caps()
        self.driver.implicitly_wait(20)
    # tearDown()方法用于测试用例之后的善后工作。如关闭数据库连接，退出应用。
    # 无论这个方法写在哪里，都是最后执行
    # @classmethod
    def tearDown(self):
        '''
        测试后的结束工作
        :return:
        '''
        self.driver.quit()

    def test_get_application_names(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        try:
            get_appnames = Work(self.driver)
            get_appnames.click_work_btn(i=1)
            appnames=get_appnames.get_all_application_names()
            print("当前页面的全部应用为：%s" % appnames)
        except Exception as e:
            print("获取工作页面所有应用的名称失败,具体信息:%s" % e)
            get_appnames.get_windows_img()  # 调用基类中的截图方法



if __name__ == '__main__':
    unittest.main()