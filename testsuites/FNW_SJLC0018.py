import unittest,time
from pageobject.task import Task
from framework.app_config import Config

class Search_Task(unittest.TestCase):
    '''
    功能描述：任务列表页面搜索某个任务
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

    def test_search_group(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        search_group = Task(self.driver)
        search_group.click_work_btn()
        time.sleep(2)
        search_group.click_chang_tenant_btn()
        time.sleep(3)
        search_group.click_tenant_choose()
        time.sleep(3)
        #点击进入任务中心
        search_group.click_task()
        time.sleep(2)
        search_group.click_search_group()
        time.sleep(3)
        search_group.type_search_group("测试")
        search_group.change_input_method("sogou")
        time.sleep(3)
        search_group.click_search_btn()
        time.sleep(2)
        search_group.change_input_method("appium")
        time.sleep(3)
        search_group.click_look_task()
        time.sleep(6)


if __name__ == '__main__':
    unittest.main()