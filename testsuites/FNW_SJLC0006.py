#-*-coding:utf-8-*-
import time
import unittest
from pageobject.home import Home
from framework.app_config import Config

class Long_Stick(unittest.TestCase):
    '''
    功能描述:置顶会话
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

    def test_stick_chat(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        long_stick = Home(self.driver)
        try:
            before_home_name = long_stick.get_last_message_name()
            # print(before_home_name)
            long_stick.long_press_last_message()
            long_stick.get_windows_img()  #
            print(long_stick.get_lens_chat())
            if long_stick.get_lens_chat() == 3:
                long_stick.stick_chat(num=1)
            else:
                long_stick.stick_chat(num=0)
            after_home_name = long_stick.get_first_message_name()
            long_stick.get_windows_img() #
            if before_home_name == after_home_name:
                print("会话置顶成功！")
            else:
                print("会话置顶失败！")
        except Exception as e:
            print("Cant find xinlingshou's message,%s" % e)

if __name__ == '__main__':
    unittest.main()
