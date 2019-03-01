#-*-coding:utf-8-*-
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os.path
import sys

current_working_directory = "C:\\Users\\Administrator\\PycharmProjects\\automation_framework_demo"
sys.path.append(current_working_directory)  #对于模块和自己的脚本不在同一目录下，使用此方法


class BasePage(object):
    '''
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    '''

    def __init__(self,driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)

    def close(self):
        try:
            self.driver.close()
        except NameError as e:
            print("Failed to quit the browser")

    #保存图片
    def get_windows_img(self):
        '''
        这里我们把file_path这个参数写死,直接保存到我们项目根目录的一个文件夹.\Screenshots下
        :return:
        '''
        file_path =os.path.dirname(os.path.abspath('.'))+'/screenshots/'

        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path +rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except NameError as e:
            self.get_windows_img()

    #切换输入法
    def change_input_method(self,name):
        input_method = ''
        if name == "搜狗" or name == 'sogou':
            input_method=self.driver.activate_ime_engine('com.sohu.inputmethod.sogou/.SogouIME')
        if name == "app" or name == 'appium':
            input_method=self.driver.activate_ime_engine('io.appium.android.ime/.UnicodeIME')
        return input_method


        #定位元素的方法
    def find_element(self,selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0].strip(' ')
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
            except NoSuchElementException as e:
                self.get_windows_img()
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
            except NoSuchElementException as e:
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == "a" or selector_by == 'android_uiautomator':
            try:
                element = self.driver.find_element_by_android_uiautomator(selector_value)
            except NoSuchElementException as e:
                self.get_windows_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    def find_elements(self, selector):
        """
        重写find_elements
        """
        elements = ''
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0].strip(' ')
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                elements = self.driver.find_elements_by_id(selector_value)
            except NoSuchElementException as e:
                print("Can't find the elements,%s" % e)
                self.get_windows_img()
        elif selector_by == "n" or selector_by == 'name':
            elements = self.driver.find_elements_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class name':
            elements = self.driver.find_elements_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            elements = self.driver.find_elements_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            elements = self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                elements = self.driver.find_elements_by_xpath(selector_value)
            except NoSuchElementException as e:
                print("Can't find the elements,%s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            elements = self.driver.find_elements_by_css_selector(selector_value)
        elif selector_by == "a" or selector_by == 'android_uiautomator':
            try:
                elements = self.driver.find_elements_by_android_uiautomator(selector_value)
            except NoSuchElementException as e:
                print("Can't find the elements,%s" % e)
                self.get_windows_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        # print(elements)
        return elements

        #输入
    def type(self, selector, text):
        el = self.find_element(selector)
        try:
            el.clear()
            el.click()
            el.send_keys(text)
        except NameError as e:
            self.get_windows_img()
        #清除文本
    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
        except NameError as e:
            self.get_windows_img()

        #点击元素
    def click(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
        except NameError as e:
            print("Failed to click the element with %s " % e)

    #点击元素
    def clicks(self,selector,num=0):
        el = self.find_elements(selector)[num]
        try:
            el.click()
        except NameError as e:
            print("Failed to click the element with %s " % e)

        #获取网页标题
    def get_page_title(self):
        return self.driver.title

    #获取元素的text
    def get_text(self,selector):
        el=self.find_element(selector)
        try:
            el = el.text
            return el
        except NameError as e:
            print("Failed to get element's text name,%s" % e)
    #获取多个元素的text


    def get_texts(self,selector):
        els = self.find_elements(selector)
        return els

    def gets_texts(self,selector):
        els_list=[]
        els = self.find_elements(selector)
        for i in els:
            el=i.text
            els_list.append(el)
        return els_list

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    def swipe_left(self):
        '''左滑'''
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        self.driver.swipe(x*4/5,y/6,x/5,y/6)

    def swipe_rigth(self):
        '''右滑'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x/5,y/6,x*4/5,y/6)

    def swipe_login_right(self,number=3):
        '''新下载app滑动闪频页'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        for i in range(number):
            self.driver.swipe(x*9/10,y/2,x/10, y/2)
            time.sleep(1)

    def swipe_up(self):
        '''上滑'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x/2,y*6/8,x/2,y/8)

    def swipe_down(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x/2,y/4,x/2,y*3/4)

    def swipe_day(self, i):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print(x/2,y*44/51,x/2,y*43/51)
        self.driver.swipe(x/2,y*44/51,x/2,y*(42-i)/51)

    def swipe_task_day(self):
        '''上滑'''
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        print(x/4,y*7/36,x/4,y/6)
        self.driver.swipe(x/3,y*44/51,x/3,y*42/51)

    def swipe_mouth(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*2/5,y/7,x*2/5,y*4/21)

    def swipe_time_down(self, x1, y1, x2, y2):
        self.driver.swipe(x1,y1,x2,y2)

    def displayed(self,selector):
        el=self.find_element(selector)
        try:
            el=el.is_displayed()
            return el
        except Exception as e:
            print("Can't find the element,%s" % e)

    def home_long_press(self,selector,i=0):
        '''长按'''
        els = self.find_elements(selector)
        # print(els)
        # TouchAction(self.driver).long_press(els[i],None,None,10000).wait(1000).perform()
        TouchAction(self.driver).long_press(els[i], None, None, 10000).perform()
        time.sleep(1)

    #获取toast text的封装,传入toast部分文本,返回全部文本
    def get_toast_text(self,text):
        try:
            toast_loc = (By.XPATH,"//*[contains(@text,'"+text+"')]")
            ele=WebDriverWait(self.driver,10,0.1).until(expected_conditions.presence_of_element_located(toast_loc))
            print(ele.text)
            return ele.text
        except:
            return None


    #封装处理弹框
    def always_allow(self,number=2):
        for i in range(number):
            loc = ("xpath","//*[@text='总是允许']")
            try:
                el=WebDriverWait(self.driver,1,0.5).until(expected_conditions.presence_of_element_located(loc))
                el.click()
            except:
                pass

    # def switch_app(self):
    #     self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

    #显性等待
    def wait(self,selector):
        el=WebDriverWait(self.driver,1,0.5).until(lambda driver:self.driver.find_element(selector))


















































