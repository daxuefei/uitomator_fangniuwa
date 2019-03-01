import unittest,time
from pageobject.work import Work
from framework.app_config import Config

class Add_Application(unittest.TestCase):
    '''
    功能描述：增加常用应用
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

    def test_login(self):
        '''
        这里一定要以test开头,把测试逻辑封装到一个test开头的方法里面。
        :return:
        '''
        add_application = Work(self.driver)
        add_application.click_work_btn(i=1)
        before_edit_application_count=len(add_application.get_all_application_names())
        add_application.click_more_btn(i=-1)

        time.sleep(2)
        #点击编辑按钮
        add_application.click_edit_btn()
        time.sleep(2)
        #增加最后一个应用
        add_application.edit_application_btn(i=-1)
        time.sleep(3)
        add_application.get_windows_img()
        #点击完成按钮
        add_application.click_edit_btn()
        time.sleep(2)
        add_application.get_windows_img()#
        #点击返回按钮
        add_application.click_back_btn()
        add_application.get_windows_img()  #
        time.sleep(3)
        after_edit_application_count=len(add_application.get_all_application_names())
        if before_edit_application_count == after_edit_application_count - 1:
            print("增加应用成功!")
        else:
            print("增加应用失败。")
            add_application.get_windows_img()  # 调用基类中的截图方法


if __name__ == '__main__':
    unittest.main()