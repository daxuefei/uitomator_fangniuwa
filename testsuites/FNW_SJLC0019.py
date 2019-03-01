import unittest, time
from pageobject.task import Task
from framework.app_config import Config


class Look_Group_Task(unittest.TestCase):
    '''
    功能描述：查看某个任务组中的所有任务
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

    def test_look_group_task(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        look_group_task = Task(self.driver)
        #点击工作按钮
        look_group_task.click_work_btn()
        time.sleep(2)
        #点击切换承租人
        look_group_task.click_chang_tenant_btn()
        time.sleep(3)
        #切换至新零售承租人
        look_group_task.click_tenant_choose()
        time.sleep(3)
        # 点击进入任务中心
        look_group_task.click_task()
        time.sleep(3)
        # 点击进入任务组
        look_group_task.click_look_group_btn()
        time.sleep(2)
        # 获取全部任务组的名称
        groups_names=look_group_task.get_groups_names()
        #点击进入第一个任务组
        look_group_task.clicks_group_task()
        time.sleep(3)
        #获取任务组中任务的名称
        group_tasks=look_group_task.get_groups_names()
        print("%s中的的任务有：%s" % (groups_names[0],group_tasks))
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
