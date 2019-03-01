#-*-coding:utf-8-*-
from framework.base_page import BasePage

class Work(BasePage):
    work_btn="id=>com.xiniunet.xntalk:id/iv_tab_icon"
    application_icon="id=>com.xiniunet.xntalk:id/view_application_icon"
    application_name="id=>com.xiniunet.xntalk:id/tv_application_name"
    search_input_box="id=>com.xiniunet.xntalk:id/ll_search"
    input_box="id=>com.xiniunet.xntalk:id/view_search"
    searched_application="id=>com.xiniunet.xntalk:id/iv_head"
    edit_btn="id=>com.xiniunet.xntalk:id/tv_fctitlebar_right"
    add_delete_btn="id=>com.xiniunet.xntalk:id/tv_fctitlebar_right"
    back_btn="id=>com.xiniunet.xntalk:id/iv_fctitlebar_left"
    application_btn="id=>com.xiniunet.xntalk:id/tv_union_name"
    delete_add_btn="id=>com.xiniunet.xntalk:id/iv_delete"


    #点击页面的工作按钮
    def click_work_btn(self, i=-1):
        self.clicks(self.work_btn,i)

    def get_all_application_names(self):
        # application_names=[]
        # app_names=self.get_texts(self.application_name)
        # for i in app_names:
        #     app_names=i.text
        #     application_names.append(app_names)
        # print(application_names)
        application_names=self.gets_texts(self.application_name)
        return application_names

    #点击某一个应用,默认为最后一个
    def click_more_btn(self,i=-1):
        self.clicks(self.application_icon,i)

    def click_input_box(self):
        self.click(self.search_input_box)

    def type_input_box(self,text):
        self.type(self.input_box,text)

    def click_search_application(self):
        self.click(self.searched_application)

    # def click_search_btn(self):
    #     self.driver.keyevent('66')

    def click_edit_btn(self):
        self.click(self.edit_btn)

    #增加或删除常用应用,默认为删除第五个应用
    def edit_application_btn(self,i=0):
        self.clicks(self.delete_add_btn,i)

    def click_back_btn(self):
        self.click(self.back_btn)

    def click_application_btn(self):
        self.click(self.application_btn)













