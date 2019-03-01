#-*-coding:utf-8-*-
import time
import unittest
from pageobject.home import Home
from framework.app_config import Config

class Long_Delete(unittest.TestCase):
    '''
    功能描述：删除首页的最后一个聊天信息
    '''
    # setUp（）方法用于测试用例执行前的初始化工作。如测试用例需要访问数据库，可以在setUp中建立数据库链接
    # 并进行初始化。如测试用例需要启动appium服务，则需要在该方法内启动appium服务
    # @classmethod
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

    def test_delete_chat(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        long_delete = Home(self.driver)
        try:
            long_delete.long_press_last_message()
            long_delete.get_windows_img()#
            long_delete.delete_message()
            long_delete.click_delete_btn()
            long_delete.get_windows_img()#
            time.sleep(2)
        except Exception as e:
            print("Cant find xinlingshou's message,%s" % e)

if __name__ == '__main__':
    unittest.main()