#-*-coding:utf-8-*-
import time
import unittest
from pageobject.home import Home
from framework.app_config import Config

class Request_Message(unittest.TestCase):
    '''
    功能描述:获取某个承租人下面的所有任务列表
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

    def test_click_message(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        request_message = Home(self.driver)
        try:
            request_message.click_xinlingshou()
            request_message.get_windows_img()#
            time.sleep(3)
            get_messages = request_message.get_message_lists()
            request_message.get_windows_img()  #
            for i in get_messages:
                el_text = i.text
                print(el_text)
        except Exception as e:
            print("Cant find xinlingshou's message,%s" % e)

if __name__ == '__main__':
    unittest.main()
