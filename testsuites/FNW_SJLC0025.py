#-*-coding:utf-8-*-
import unittest, time
from pageobject.task import Task
from framework.app_config import Config

class Stick_Task(unittest.TestCase):
    '''
    功能描述：置顶任务、取消置顶任务
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

    def test_stick_task(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        stick_task = Task(self.driver)
        #点击工作按钮
        stick_task.click_work_btn()
        time.sleep(2)
        #点击切换承租人
        stick_task.click_chang_tenant_btn()
        time.sleep(3)
        #切换至新零售承租人
        stick_task.click_tenant_choose()
        time.sleep(3)
        # 点击进入任务中心
        stick_task.click_task()
        time.sleep(3)
        #长按第一个任务
        stick_task.long_press_task()
        time.sleep(2)
        #点击置顶任务按钮
        stick_task.click_task_choose(num=1)
        stick_task.get_windows_img()
        end_text=stick_task.get_toast_text('已置顶')
        self.assertIn('已置顶', end_text)
        time.sleep(3)
        # 下面是取消置顶操作
        stick_task.long_press_task(0)
        time.sleep(2)
        stick_task.click_task_choose(num=1)
        end_text = stick_task.get_toast_text('取消置顶')
        self.assertIn('取消置顶', end_text)


if __name__ == '__main__':
    unittest.main()
