#-*-coding:utf-8-*-
import unittest, time
from pageobject.task import Task
from framework.app_config import Config

class Dissolve_Group(unittest.TestCase):
    '''
    功能描述：解散任务组
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

    def test_dissolve_group(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        dissolve_group = Task(self.driver)
        #点击工作按钮
        dissolve_group.click_work_btn()
        time.sleep(2)
        #点击切换承租人
        dissolve_group.click_chang_tenant_btn()
        time.sleep(3)
        #切换至新零售承租人
        dissolve_group.click_tenant_choose()
        time.sleep(3)
        # 点击进入任务中心
        dissolve_group.click_task()
        time.sleep(3)
        # 点击进入任务组
        dissolve_group.click_look_group_btn()
        time.sleep(2)
        #点击进入第一个任务组
        dissolve_group.clicks_group_task()
        time.sleep(2)
        #点击任务组中的编辑按钮
        dissolve_group.click_group_edit_btn()
        time.sleep(2)
        #点击解散任务组的按钮
        dissolve_group.click_dissolve_btn()
        #点击确认按钮
        dissolve_group.click_ensure_btn()
        dissolve_text=dissolve_group.get_toast_text('解散成功')
        self.assertIn('解散成功',dissolve_text)



if __name__ == '__main__':
    unittest.main()
