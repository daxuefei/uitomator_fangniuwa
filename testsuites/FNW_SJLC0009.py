#-*-coding:utf-8-*-
import time
import unittest
from pageobject.home import Home
from framework.app_config import Config

class Send_message(unittest.TestCase):
    '''
    功能描述：给消息页面的第一个人发送消息
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

    def test_send_message(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        send_message = Home(self.driver)
        try:
            send_message.click_chat(i=2)
            send_message.get_windows_img()
            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            text = '测试自动聊天，发送时间:' + current_time
            send_message.type_chat_box(text)
            # send_message.change_input_method("sogou")  #切换至搜狗输入法
            time.sleep(3)
            send_message.click_chat_box()
            time.sleep(2)
            send_message.click_send_btn()
            time.sleep(2)
            last_message_text=send_message.get_last_message_text(i=-1)
            send_message.get_windows_img()#
            if text == last_message_text:
                print("会话发送成功！")
            else:
                print("会话发送失败。")
            time.sleep(3)
        except Exception as e:
            print("Cant find xinlingshou's message,%s" % e)


if __name__ == '__main__':
    unittest.main()