#-*-coding:utf-8-*-
import unittest,time
from pageobject.work import Work
from framework.app_config import Config

class Search_Appnames(unittest.TestCase):
    '''
    功能描述：精确搜索应用——请假
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

    def test_search_name(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        try:
            search_appnames = Work(self.driver)
            search_appnames.click_work_btn(i=1)
            search_appnames.click_more_btn(i=-1)
            search_appnames.get_windows_img()#调用基类中的截图方法
            search_appnames.click_input_box()
            time.sleep(2)
            search_appnames.change_input_method("appium")
            search_appnames.type_input_box("请假")
            search_appnames.click_application_btn()
            time.sleep(2)
            search_appnames.get_windows_img()
        except Exception as e:
            print("精确搜索应用请假失败，具体信息如下：%s" % e)


if __name__ == '__main__':
    unittest.main()