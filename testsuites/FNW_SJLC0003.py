#-*-coding:utf-8-*-
import time
import unittest
from pageobject.home import Home
from selenium import webdriver
from appium import webdriver
from framework.app_config import Config


class Complete_Home_Task(unittest.TestCase):
    '''
    功能描述：完成延期任务
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

        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # # desired_caps['platformVersion'] = '4.4.2'
        # desired_caps['platformVersion'] = '6.0.1'
        # # desired_caps['platformVersion'] = '7.1.1'
        # desired_caps['deviceName'] = 'test'  # 连接多个设备才有用
        # # desired_caps['app'] = r'e:\apk\toutiao.apk'#如果已经安装好软件乐意不需要，这边填写的是apk在电脑上的路径
        # desired_caps['appPackage'] = 'com.xiniunet.xntalk'  # app的包名，唯一标志app
        # desired_caps['appActivity'] = 'com.xiniunet.xntalk.common.activity.splash.SplashActivity'  # 对应安卓应用的操作界面
        # desired_caps['unicodeKeyboard'] = True  # 安装一个中文的输入法
        # desired_caps['resetKeyboard'] = True  #
        # desired_caps['noReset'] = True  # 清除元素数据，跳过初始页面
        # desired_caps['newCommandTimeout'] = 6000
        # desired_caps['automationName'] = 'uiautomator2'
        # # 启动Remote RPC
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 把上述参数传给appium services
        # self.driver.implicitly_wait(50)
    # tearDown()方法用于测试用例之后的善后工作。如关闭数据库连接，退出应用。
    # 无论这个方法写在哪里，都是最后执行
    # @classmethod
    def tearDown(self):
        '''
        测试后的结束工作
        :return:
        '''
        self.driver.quit()

    def test_task_complete(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        complete_task = Home(self.driver)
        try:
            time.sleep(5)
            #获取当前页面的卡片的总数量
            before_total_card = complete_task.card_total_num()
            complete_task.click_colligate_btn()
            time.sleep(3)
            complete_task.change_input_method('appium')
            time.sleep(2)
            #填写完成理由
            current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            text = '任务已完成，完成时间:'+ current_time
            complete_task.type_colligate_text(text)
            time.sleep(3)
            complete_task.get_windows_img()  #
            complete_task.click_complete_btn()
            #获取页面的toast
            complete_task.get_toast_text("完成")
            complete_task.get_windows_img()  #
            #如果页面卡片的数量减少，延期任务成功
            after_total_card = complete_task.card_total_num()
            if int(after_total_card) == int(before_total_card) -1:
                print("自动操作完成任务成功!")
            else:
                print("自动操作完成任务失败!")
        except Exception as e:
            print("Can't find the card,%s"% e)


if __name__ == '__main__':
    unittest.main()
