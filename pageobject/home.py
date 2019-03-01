 #-*-coding:utf-8-*-
from framework.base_page import BasePage

class Home(BasePage):

    task_card = "id=>com.xiniunet.xntalk:id/task_head_rl"
    card_current = "id=>com.xiniunet.xntalk:id/tv_current"
    card_total = "id=>com.xiniunet.xntalk:id/tv_total"
    colligate_btn = "id=>com.xiniunet.xntalk:id/task_colligate_btn"
    colligate_text = "id=>com.xiniunet.xntalk:id/edt"
    complete_btn = "id=>com.xiniunet.xntalk:id/tv_copmlete"
    delay_btn = "id=>com.xiniunet.xntalk:id/task_send_message_btn"
    delay_reason = "id=>com.xiniunet.xntalk:id/edt"
    delay_time_choose ="id=>com.xiniunet.xntalk:id/tv_choose_delay_time"
    delay_time_day ="id=>com.xiniunet.xntalk:id/day"
    delay_time_month="id=>com.xiniunet.xntalk:id/month"
    delay_time_sure ="id=>com.xiniunet.xntalk:id/tv_sure"
    delay_time_card ="id=>com.xiniunet.xntalk:id/timepicker"
    # chat_message ="id=>//*[rescource-id='com.xiniunet.xntalk:id/tv_chat_request_message_name'[contains(@text,'新零售测试')]]"
    chat_message ="id=>com.xiniunet.xntalk:id/tv_chat_request_message_name"
    message_list ="id=>com.xiniunet.xntalk:id/tv_title"
    long_press_card="id=>com.xiniunet.xntalk:id/custom_dialog_text_view"
    delete_btn="id=>android:id/button1"
    input_box="id=>com.xiniunet.xntalk:id/editTextMessage"
    send_btn="id=>com.xiniunet.xntalk:id/buttonSendMessage"
    chat_message_text="id=>com.xiniunet.xntalk:id/nim_message_item_text_body"


    #获取页面卡片
    def get_task_card(self):
        iscard= self.find_element(self.task_card)
        return iscard

    #右滑卡片
    def swipe_left_card(self):
        self.swipe_left()
    #左滑卡片
    def swipe_rigth_card(self):
        self.swipe_rigth()

    # 修改延期的时间的日期(天)
    def swipe_delay_day(self,i):
        self.click(self.delay_time_day)
        self.swipe_day(i)

    #修改延期的时间的日期(月)
    def swipe_delay_month(self):
        self.click(self.delay_time_month)
        self.swipe_mouth()

    #写死修改延期时间
    def swipe_delay(self):
        self.click(self.delay_time_day)
        self.swipe_time_down(x1=360, y1=1105, x2=360, y2=1055)

    #获取当前的卡片数字
    def card_current_num(self):
        current_num=self.get_text(self.card_current)
        return current_num

    #获取总的卡片数字
    def card_total_num(self):
        num=self.get_text(self.card_total)
        total_num = num.split('/')[1]
        return total_num

    #点击延期卡片的完成按钮
    def click_colligate_btn(self):
        self.click(self.colligate_btn)

    def type_colligate_text(self,text):
        self.type(self.colligate_text,text)

    def click_complete_btn(self):
        self.click(self.complete_btn)

    #点击延期卡片的延期按钮
    def click_delay_btn(self):
        self.click(self.delay_btn)
    #填写延期理由
    def type_delay_reason(self,text):
        self.type(self.delay_reason,text)

    #点击选择延期时间
    def click_delay_time(self):
        self.click(self.delay_time_choose)

    #点击设置延期时间
    def click_delay_time_sure(self):
        self.click(self.delay_time_sure)

    #获取延期时间
    def get_delay_time(self):
        delay_time=self.get_text(self.delay_time_choose)
        return delay_time

    def isdisplayed(self):
        el=self.displayed(self.task_card)
        print(el)

    #点击进入承租人消息
    def click_xinlingshou(self,num=0):
        self.clicks(self.chat_message,num)

    #获取首页承租人消息中的任务列表
    def get_message_lists(self):
        message_lists = self.get_texts(self.message_list)
        return message_lists


    def long_press_last_message(self,i=-1):
        self.home_long_press(self.chat_message,i)

    def get_last_message_name(self,i=-1):
        home_message_names=self.get_texts(self.chat_message)
        return home_message_names[i].text

    def get_first_message_name(self,i=2):
        home_message_names=self.get_texts(self.chat_message)
        return home_message_names[i].text

    def stick_chat(self,num):
        self.clicks(self.long_press_card,num)

    def get_lens_chat(self):
        lens_text=[]
        els= self.find_elements(self.long_press_card)
        for i in els:
            el = i.text
            lens_text.append(el)
        lens_of_chat = len(lens_text)
        return lens_of_chat

    def long_press_stick_message(self,i=2):
        self.home_long_press(self.chat_message,i)

    def delete_message(self,num=-1):
        self.clicks(self.long_press_card,num)

    def click_delete_btn(self):
        self.click(self.delete_btn)

    def click_chat(self,i):
        self.clicks(self.chat_message,i)

    def type_chat_box(self,text):
        self.click(self.input_box)
        self.type(self.input_box,text)

    def click_chat_box(self):
        self.click(self.input_box)

    def click_send_btn(self):
        self.click(self.send_btn)

    def get_last_message_text(self,i):
        last_message_text=self.get_texts(self.chat_message_text)
        return last_message_text[i].text






