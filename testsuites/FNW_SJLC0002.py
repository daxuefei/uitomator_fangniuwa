#-*-coding:utf-8-*-
import time
import unittest
from pageobject.home import Home
from selenium import webdriver
from appium import webdriver
from framework.app_config import Config

class Look_Card(unittest.TestCase):
    '''
    功能描述：滑动延期任务卡片
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

    def test_task_swipe(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        look_card = Home(self.driver)
        try:
            #获取页面卡片的数量,如果数量大于1就左右滑动
            card_total = look_card.card_total_num()
            look_card.get_windows_img()
            if int(card_total) > 1:
                before_card_num = look_card.card_current_num()
                print(before_card_num)
                look_card.swipe_left_card()
                time.sleep(3)
                after_card_num = look_card.card_current_num()
                print(after_card_num)
                if int(after_card_num) == int(before_card_num) + 1:
                    print("延期卡片左滑成功!")
                else:
                    print("延期卡片左滑失败。")
                look_card.get_windows_img()
            else:
                print("There is  only one card")
        except Exception as e:
            print("Can't find yhe card,%s"% e)


if __name__ == '__main__':
    unittest.main()
