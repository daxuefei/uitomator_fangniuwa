# -*-coding:utf-8-*-
import unittest, time
from pageobject.my import My
from framework.app_config import Config


class Logout(unittest.TestCase):
    '''
    功能描述：查看已完成任务组
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
    #  @classmethod
    def tearDown(self):
        '''
        测试后的结束工作
        :return:
        '''
        self.driver.quit()

    def test_logout(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        logout = My(self.driver)
        # 点击我的按钮
        logout.click_work_btn(i=-1)
        time.sleep(2)
        logout.get_windows_img()
        #点击设置按钮
        logout.click_set_btn()
        time.sleep(2)
        logout.get_windows_img()
        #点击登出按钮
        logout.click_logout_btn()
        time.sleep(2)
        logout.get_windows_img()
        #点击退出当前账号按钮
        logout.click_exit_btn()
        time.sleep(2)
        logout.get_windows_img()
        logout.click_ensure_exit_btn()
        time.sleep(1)
        logout.get_windows_img()



if __name__ == '__main__':
    unittest.main()
