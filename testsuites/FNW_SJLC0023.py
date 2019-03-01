#-*-coding:utf-8-*-
import unittest, time
from pageobject.task import Task
from framework.app_config import Config


class Delay_Task(unittest.TestCase):
    '''
    功能描述：延期任务(暂时无法完成，无法滑动延期的时间和点击设置延期按钮<uitomator也无法定位到此页面)
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

    def test_delay_task(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        delay_task = Task(self.driver)
        #点击工作按钮
        delay_task.click_work_btn()
        time.sleep(2)
        #点击切换承租人
        delay_task.click_chang_tenant_btn()
        time.sleep(3)
        #切换至新零售承租人
        delay_task.click_tenant_choose()
        time.sleep(3)
        # 点击进入任务中心
        delay_task.click_task()
        time.sleep(3)
        #点击创建任务按钮
        delay_task.click_create_task()
        #输入任务标题
        delay_task.change_input_method('appium')
        delay_task.type_task_title('创建一个延期测试的任务')
        #输入任务内容
        delay_task.type_input_content('这是一个新的延期任务')
        #点击完成按钮
        delay_task.click_complete_btn()
        time.sleep(3)
        task_choose_lens=0
        i = 0
        while task_choose_lens != 6:
            delay_task.long_press_task(i)
            task_choose_lens = len(delay_task.get_task_chooses())
            if task_choose_lens != 6:
                delay_task.click_cancel_btn()
                delay_task.swipe_flash_task()
                i = i+1
        #点击延期任务
        delay_task.click_task_choose(num=3)
        time.sleep(3)
        #输入延期任务理由
        delay_task.type_input_reason('延期此任务')
        #点击选择延期时间
        delay_task.click_delay_choose_btn()
        time.sleep(2)
        # print(self.driver.current_context)
        self.driver.switch_to.context('NATIVE_APP')
        print("---------------------------------------------")
        print(self.driver.page_source)
        # self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        # end_task.swipe_delay_day()
        # time.sleep(2)
        # end_task.click_set_btn()
        # time.sleep(2)
        # end_task.click_task_complete_btn()
        # time.sleep(2)
        # end_text=end_task.get_toast_text('已延期')
        # self.assertIn('解散成功', end_text)

if __name__ == '__main__':
    unittest.main()
