#-*-coding:utf-8-*-
from framework.base_page import BasePage
import time

class Task(BasePage):
    work_btn="id=>com.xiniunet.xntalk:id/iv_tab_icon"
    application_icon="id=>com.xiniunet.xntalk:id/view_application_icon"
    change_tenant_btn="id=>com.xiniunet.xntalk:id/view_layout"
    tenant_choose="android_uiautomator=>new UiSelector().text(\"新零售测试\")"
    create_task_btn="xpath=>//*[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[contains(@index,2)]/android.view.ViewGroup[contains(@index,1)]/android.widget.ImageView"
    input_title="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[contains(@index,0)]/android.widget.EditText"
    input_content="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[contains(@index,1)]/android.widget.EditText"
    more_btn="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[contains(@index,1)]/android.widget.EditText"
    add_executor_btn="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[contains(@index,0)]/android.view.ViewGroup[contains(@index,1)]/android.widget.EditText"
    add_executor="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[contains(@index,1)]"
    # choose_section="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[11]/android.view.ViewGroup[1]/android.widget.TextView"(此方法不可行)
    choose_section="android_uiautomator=>new UiSelector().text(\"下级\")"
    choose_person="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]"
    confirm_btn="android_uiautomator=>new UiSelector().text(\"确认\")"
    complete_btn="android_uiautomator=>new UiSelector().text(\"完成\")"
    text_names="xpath=>//android.widget.ScrollView[1]//*[@class='android.widget.TextView' and @index='1']"
    look_group_btn="xpath=>//*[@class='android.widget.ImageView']"
    create_group_btn="xpath=>//*[@class='android.widget.ImageView']"
    input_group_title="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText"
    choose_task_btn="xpath=>//*[@text='选择关联任务']"
    choose_task="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]"
    choose_btn="xpath=>//*[@text='选择']"
    create_btn="xpath=>//*[@text='新建']"
    get_group_name="xpath=>//android.widget.ScrollView[1]//*[@class='android.widget.TextView' and @index='1']"
    search_input="xpath=>//*[@class='android.widget.TextView' and @text='搜索']"
    input_group="xpath=>//*[@class='android.widget.EditText' and @text='搜索']"
    task_look="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]"
    edit_btn="xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ImageView"
    edit_group_btn="xpath=>//android.widget.FrameLayout[4]//*[@class='android.widget.ImageView' and @index='1']"
    dissolve_btn="xpath=>//*[@text='解散任务组']"
    ensure_btn="id=>android:id/button1"
    long_press_task_btn="xpath=>//android.widget.ScrollView[1]/android.view.ViewGroup[1]//*[@class='android.widget.TextView' and @index='1']"
    get_text_names="xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]//*[@class='android.widget.TextView' and @index='0']"
    cancel_btn="xpath=>//*[@text='取消']"
    reason_input="xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//*[@class='android.widget.EditText' and @text='输入内容']"
    complete_task_btn="xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]//*[@class='android.widget.TextView' and @text='完成']"
    delay_choose_btn="xpath=>//android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]//*[@class='android.widget.EditText' and @text='选择延期时间']"
    set_btn="xpath=>//*[@text='设置延期时间']"
    delay_group="xpath=>//android.widget.ScrollView[1]//*[@class='android.widget.TextView' and @text='逾期任务组']"
    complete_group="xpath=>//android.widget.ScrollView[1]//*[@class='android.widget.TextView' and @text='完成任务组']"
    end_group="xpath=>//android.widget.ScrollView[1]//*[@class='android.widget.TextView' and @text='终止任务组']"

    #点击页面的工作按钮
    def click_work_btn(self, i=1):
        self.clicks(self.work_btn,i)

    #点击应用,任务中心
    def click_task(self,i=1):
        self.clicks(self.application_icon,i)
    #点击切换承租人按钮
    def click_chang_tenant_btn(self):
        self.click(self.change_tenant_btn)

    #点击选择新零售承租人
    def click_tenant_choose(self):
        self.click(self.tenant_choose)

    #点击创建任务按钮
    def click_create_task(self):
        self.click(self.create_task_btn)

    #输入任务标题
    def type_task_title(self,text):
        self.type(self.input_title,text)

    #点击查看更多
    def click_more_btn(self):
        self.click(self.more_btn)
    #点击添加执行人按钮
    def click_add_btn(self):
        self.click(self.add_executor_btn)
    #点击选择人员
    def click_add_executor(self):
        self.click(self.add_executor)

    def click_choose_section(self,i=10):
        self.clicks(self.choose_section,i)

    def click_choose_person(self):
        self.click(self.choose_person)

    def click_confirm_btn(self):
        self.click(self.confirm_btn)

    def click_complete_btn(self):
        self.click(self.complete_btn)

    def get_task_name(self):
        task_names=[]
        els=self.get_texts(self.text_names)
        for i in els:
            el=i.text
            task_names.append(el)
        return task_names

    def click_look_group_btn(self,number=1):
        self.clicks(self.look_group_btn,number)

    def click_create_group(self,number=1):
        self.clicks(self.create_group_btn,number)

    def type_input_group_title(self,text):
        self.type(self.input_group_title,text)

    def click_choose_task_btn(self):
        self.click(self.choose_task_btn)

    def click_choose_task(self):
        self.click(self.choose_task)

    def click_choose_btn(self):
        self.click(self.choose_btn)

    def click_create_btn(self):
        self.click(self.create_btn)

    def get_groups_names(self):
        names=self.gets_texts(self.get_group_name)
        return names

    def click_search_group(self):
        self.click(self.search_input)

    def type_search_group(self,text):
        self.type(self.input_group,text)

    def click_search_btn(self):
        self.driver.keyevent('66')

    def click_look_task(self):
        self.click(self.task_look)

    #点击进入任务组的第一个任务组中
    def clicks_group_task(self,number=0):
        self.clicks(self.get_group_name,number)

    def swipe_up_task(self):
        self.swipe_up()

    def get_tasks(self):
        els_names = []
        before_els_names = []
        after_els_names = []
        els=self.get_texts(self.get_group_name)
        for i in els:
            el=i.text
            els_names.append(el)
            after_els_names.append(el)
        while after_els_names != before_els_names:
            self.swipe_up_task()
            time.sleep(2)
            before_els_names = after_els_names
            els = self.get_texts(self.get_group_name)
            for i in els:
                el = i.text
                els_names.append(el)
                after_els_names.append(el)
            # print(els_names)
            return els_names

    def get_task_names(self,task_name):
        els = self.get_texts(self.get_group_name)
        for i in els:
            el = i.text
            task_name.append(el)
        return task_name

    def click_group_edit_btn(self):
        self.click(self.edit_btn)

    def click_edit_btn(self,num=1):
        self.clicks(self.edit_group_btn,num)
    #点击解散任务组
    def click_dissolve_btn(self):
        self.click(self.dissolve_btn)

    def click_ensure_btn(self):
        self.click(self.ensure_btn)

    def long_press_task(self,i=0):
        self.home_long_press(self.long_press_task_btn,i)

    def get_task_chooses(self):
        task_choose=self.gets_texts(self.get_text_names)
        return task_choose

    #默认点击终止任务
    def click_task_choose(self,num=4):
        self.clicks(self.get_text_names,num)

    def click_cancel_btn(self):
        self.click(self.cancel_btn)

    def swipe_flash_task(self):
        self.swipe_down()

    def type_input_reason(self,text):
        self.type(self.reason_input,text)

    def click_task_complete_btn(self):
        self.click(self.complete_task_btn)

    def type_input_content(self,text):
        self.type(self.input_content,text)

    def click_delay_choose_btn(self):
        self.click(self.delay_choose_btn)

    def swipe_delay_day(self):
        self.swipe_task_day()
        # self.swipe_time_down(x1=180,y1=189,x2=180,y2=240)

    def click_set_btn(self):
        self.click(self.set_btn)


    #任务中心页面点击进入逾期任务组
    def click_delay_group(self):
        self.click(self.delay_group)

    def click_complete_group(self):
        self.click(self.complete_group)

    def click_end_group(self):
        self.click(self.end_group)

    def swipe_current_page(self):
        els_name = []
        get_ele_name = self.get_task_names(els_name)
        after_els_names = []
        get_after_names = self.get_task_names(after_els_names)
        get_before_names = []
        while get_after_names != get_before_names:
            self.swipe_up_task()
            self.get_windows_img()  #
            time.sleep(2)
            get_before_names = get_after_names
            after_els_names = []
            get_after_names = self.get_task_names(after_els_names)
            get_ele_name = self.get_task_names(get_ele_name)
        return get_ele_name

















