#-*-coding:utf-8-*-
import time
import unittest
from pageobject.login import Login
from selenium import webdriver
from appium import webdriver
from framework.app_config import Config

class LoginTest(unittest.TestCase):
    '''
    功能描述：登录
    '''
    # setUp（）方法用于测试用例执行前的初始化工作。如测试用例需要访问数据库，可以在setUp中建立数据库链接
    # 并进行初始化。如测试用例需要启动appium服务，则需要在该方法内启动appium服务
    @classmethod
    def setUp(self):
        '''
        测试前的准备工作
        :return:
        '''
        config=Config()
        self.driver=config.desired_caps()
        self.driver.implicitly_wait(20)
    # @classmethod
    def tearDown(self):
        '''
        测试后的结束工作
        :return:
        '''
        # config = Config()
        # cls.driver = config.desired_caps()
        self.driver.quit()

    def test_login(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''

        login = Login(self.driver)
        #滑动闪屏页，只有第一次安装才需要
        # login.swipe_login_right()
        #点击app需要的权限
        # login.always_allow()
        time.sleep(7)
        login.change_input_method('appium')
        time.sleep(2)
        login.type_account('15370135956')
        login.type_password('123456')
        login.get_windows_img()
        login.click_login()
        time.sleep(2)
        login.get_windows_img()#调用基类中的截图方法
        time.sleep(3)
        login.check_name()

if __name__ == '__main__':
    unittest.main()


