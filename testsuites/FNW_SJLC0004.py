#-*-coding:utf-8-*-
import datetime
import time
import unittest
from pageobject.home import Home
from selenium import webdriver
from appium import webdriver
from framework.app_config import Config

class Delay_Home_Task(unittest.TestCase):
    '''
    功能描述：延期任务
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

    def test_task_delay(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        缺陷：目前只能实现当前日期在29号之前的日期,后续优化
        '''
        delay_task = Home(self.driver)
        try:
            before_total_card = delay_task.card_total_num()
            delay_task.get_windows_img()  #
            delay_task.click_delay_btn()
            current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            print(current_time)
            current_time_day = current_time.split(" ")[0].split("-")[2]
            text = '任务已延期，延期时间:'+ current_time
            delay_task.type_delay_reason(text)
            time.sleep(3)
            if int(current_time_day) < 29:
                delta_day = 0
                i = 0
                while delta_day < 1:
                    delay_task.click_delay_time()
                    time.sleep(2)
                    delay_task.swipe_delay_day(i)
                    time.sleep(1)
                    delay_task.click_delay_time_sure()
                    time.sleep(1)
                    delay_time = delay_task.get_delay_time()
                    current_delay_time = datetime.datetime.strptime(delay_time,'%Y-%m-%d %H:%M')
                    now_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
                    current_time = datetime.datetime.strptime(now_time,'%Y-%m-%d %H:%M')
                    delta = current_delay_time - current_time
                    delta_day = delta.days
                    time.sleep(2)
                    i = i + 2
                delay_task.get_windows_img()
                delay_task.click_complete_btn()
            delay_task.get_windows_img()
            # else:
            #     delay_task.click_delay_time()
            #     time.sleep(2)
            #     delay_task.swipe_delay_month()
            #     time.sleep(1)
            #     delay_task.click_delay_time_sure()
            #     time.sleep(1)

            after_total_card = delay_task.card_total_num()
            if int(after_total_card) == int(before_total_card) -1:
                print("自动操作延期任务成功!")
            else:
                print("自动操作延期任务失败!")
        except Exception as e:
            print("Can't find the card,%s"% e)

if __name__ == '__main__':
    unittest.main()
