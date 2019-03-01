#-*-coding:utf-8-*-
import unittest,time
from pageobject.task import Task
from selenium import webdriver
from appium import webdriver
from framework.app_config import Config
class Create_Task(unittest.TestCase):
    '''
    功能描述：新建任务
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

    def test_create_task(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        create_task = Task(self.driver)
        create_task.click_work_btn()
        time.sleep(2)
        create_task.click_chang_tenant_btn()
        time.sleep(3)
        create_task.click_tenant_choose()
        time.sleep(3)
        create_task.click_task()
        time.sleep(3)
        create_task.click_create_task()
        create_task.get_windows_img()  #
        time.sleep(3)
        text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        create_task.type_task_title(text)
        create_task.click_add_btn()
        time.sleep(3)
        create_task.click_add_executor()
        time.sleep(3)
        create_task.click_choose_section()
        time.sleep(3)
        create_task.click_choose_person()
        create_task.click_confirm_btn()
        time.sleep(3)
        create_task.click_complete_btn()
        time.sleep(3)
        create_task.click_complete_btn()
        create_task.get_windows_img()#
        create_text=create_task.get_toast_text('成功')
        self.assertIn('创建成功', create_text)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()