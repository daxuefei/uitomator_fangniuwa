#-*-coding:utf-8-*-
import unittest,time
from pageobject.task import Task
from framework.app_config import Config

class Create_Group(unittest.TestCase):
    '''
    功能描述：创建任务组
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

    def test_create_group(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        create_group = Task(self.driver)
        #点击工作
        create_group.click_work_btn()
        time.sleep(2)
        #点击切换承租人按钮
        create_group.click_chang_tenant_btn()
        time.sleep(3)
        # #切换至新零售测试承租人
        create_group.click_tenant_choose()
        time.sleep(3)
        #点击进入任务中心
        create_group.click_task()
        task_names=create_group.get_tasks()
        create_group.get_windows_img()  #
        num = 0
        for i in task_names:
            if i in ['逾期任务组','完成任务组','终止任务组']:
                num=num+1
                a=len(task_names)-num
                if a <= 0:
                    create_group.click_create_task()
                    # 输入任务标题
                    create_group.type_task_title('创建一个测试查看任务详情的任务')
                    # 输入任务内容
                    create_group.type_input_content('这是一个查看详情的任务')
                    # 点击完成按钮
                    create_group.click_complete_btn()
        time.sleep(2)
        #点击进入任务组
        create_group.click_look_group_btn()
        create_group.get_windows_img()
        time.sleep(2)
        before_names = create_group.get_groups_names()
        print(before_names)
        #点击创建任务组
        create_group.click_create_group()
        time.sleep(3)
        #输入任务组名称
        create_group.type_input_group_title('创建任务组')
        #点击选择任务组任务按钮
        create_group.click_choose_task_btn()
        time.sleep(3)
        #选择任务组中的任务
        create_group.click_choose_task()
        create_group.click_choose_btn()
        time.sleep(3)
        create_group.click_create_btn()
        time.sleep(3)
        create_group.get_windows_img()  #
        after_names=create_group.get_groups_names()
        print(after_names)
        if '创建任务组' in after_names:
            print("创建任务组成功！")
        else:
            print("创建任务组失败!")


if __name__ == '__main__':
    unittest.main()