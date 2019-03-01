#-*-coding:utf-8-*-
from framework.base_page import BasePage
import time

class My(BasePage):
    work_btn="id=>com.xiniunet.xntalk:id/iv_tab_icon"
    set_btn="id=>com.xiniunet.xntalk:id/ll_setting"
    logout_btn="id=>com.xiniunet.xntalk:id/bt_logout"
    exit_btn="id=>com.xiniunet.xntalk:id/exit"
    ensure_exit_btn="id=>android:id/button1"

    #点击页面的工作按钮
    def click_work_btn(self, i=1):
        self.clicks(self.work_btn,i)

    #点击设置
    def click_set_btn(self):
        self.clicks(self.set_btn)
    #点击退出按钮
    def click_logout_btn(self):
        self.click(self.logout_btn)
    #点击退出当前账号按钮
    def click_exit_btn(self):
        self.click(self.exit_btn)

    #点击退出按钮
    def click_ensure_exit_btn(self):
        self.click(self.ensure_exit_btn)





