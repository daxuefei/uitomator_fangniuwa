# -*-coding:utf-8-*-
import unittest, time
from pageobject.task import Task
from framework.app_config import Config

class Look_End_Group(unittest.TestCase):
    '''
    功能描述：查看已终止任务组
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

    def test_look_end_group(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        look_end_group = Task(self.driver)
        # 点击工作按钮
        look_end_group.click_work_btn()
        time.sleep(2)
        look_end_group.get_windows_img()
        # 点击切换承租人
        look_end_group.click_chang_tenant_btn()
        time.sleep(3)
        look_end_group.get_windows_img()
        # 切换至新零售承租人
        look_end_group.click_tenant_choose()
        time.sleep(3)
        look_end_group.get_windows_img()
        # 点击进入任务中心
        look_end_group.click_task()
        task_name_list=look_end_group.swipe_current_page()
        time.sleep(2)
        #获取任务列表的全部任务名称
        # task_name_list=look_end_group.get_task_name()
        #如果有终止任务组就进入终止任务组,没有就打印"页面无终止任务组，无法查看",并退出
        if '终止任务组' in task_name_list:
            look_end_group.click_end_group()
            look_end_group.swipe_current_page()
        else:
            print("页面无终止任务组，无法查看")
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
