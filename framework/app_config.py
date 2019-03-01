#-*-coding:utf-8-*-
import unittest

from selenium import webdriver
from appium import webdriver

class Config(unittest.TestCase):
    # setUp（）方法用于测试用例执行前的初始化工作。如测试用例需要访问数据库，可以在setUp中建立数据库链接
    # 并进行初始化。如测试用例需要启动appium服务，则需要在该方法内启动appium服务
    def desired_caps(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '4.4.2'
        # desired_caps['platformVersion'] = '6.0.1'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'test'  # 连接多个设备才有用
        # desired_caps['app'] = r'e:\apk\toutiao.apk'#如果已经安装好软件乐意不需要，这边填写的是apk在电脑上的路径
        desired_caps['appPackage'] = 'com.xiniunet.xntalk'  # app的包名，唯一标志app
        desired_caps['appActivity'] = 'com.xiniunet.xntalk.common.activity.splash.SplashActivity'  # 对应安卓应用的操作界面
        desired_caps['unicodeKeyboard'] = True  # 安装一个中文的输入法
        desired_caps['resetKeyboard'] = True  #
        desired_caps['noReset'] = True  # 清除元素数据，跳过初始页面
        desired_caps['newCommandTimeout'] = 6000
        # desired_caps['automationName'] = 'uiautomator2'
        # 启动Remote RPC
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 把上述参数传给appium services
        return self.driver
