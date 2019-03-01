#-*-coding:utf-8-*-
from framework.base_page import BasePage

class Login(BasePage):
    # input_box = "id=>kw"
    # search_submit_btn = "xpath=>//*[@id='su']"
    # # 百度新闻入口
    # news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"
    #
    # def type_search(self, text):
    #      self.type(self.input_box, text)
    #
    # def send_submit_btn(self):
    #     self.click(self.search_submit_btn)
    #
    # def click_news(self):
    #     self.click(self.news_link)
    #     self.sleep(2)

    input_account = "id=>com.xiniunet.xntalk:id/et_account"
    input_password = "id=>com.xiniunet.xntalk:id/et_password"
    login_btn = "id=>com.xiniunet.xntalk:id/btn_login"
    change_union_btn = "id =>com.xiniunet.xntalk:id/tv_union_account_login"
    check_element = "id=>com.xiniunet.xntalk:id/tv_title"

    #输入手机号码
    def type_account(self, text):
        self.type(self.input_account, text)

    def type_password(self,text):
        self.type(self.input_password,text)

    def click_login(self):
        self.click(self.login_btn)
        self.sleep(2)

    def check_name(self):
        title=self.get_text(self.check_element)
        try:
            if "放牛娃"  in title:
                print("登录成功.")
        except Exception as e:
            print('Test Fail.', format(e))