#-*-coding:utf-8-*-

from lib import HTMLTestRunner
import os
import unittest
import time
from testsuites.FNW_SJLC0001 import LoginTest
from testsuites.FNW_SJLC0002 import Look_Card
from testsuites.FNW_SJLC0003 import Complete_Home_Task
from testsuites.FNW_SJLC0004 import Delay_Home_Task
from testsuites.FNW_SJLC0005 import Request_Message
from testsuites.FNW_SJLC0006 import Long_Stick
from testsuites.FNW_SJLC0007 import Long_Unstick
from testsuites.FNW_SJLC0008 import Long_Delete
from testsuites.FNW_SJLC0009 import Send_message
from testsuites.FNW_SJLC0010 import Get_Appnames
from testsuites.FNW_SJLC0011 import Search_Appnames
from testsuites.FNW_SJLC0012 import Delete_Application
from testsuites.FNW_SJLC0013 import Add_Application
from testsuites.FNW_SJLC0014 import Create_Task
from testsuites.FNW_SJLC0015 import Get_Tasks
from testsuites.FNW_SJLC0016 import Create_Group
from testsuites.FNW_SJLC0017 import Look_Group
from testsuites.FNW_SJLC0018 import Search_Task
from testsuites.FNW_SJLC0019 import Look_Group_Task
from testsuites.FNW_SJLC0020 import Search_Group
from testsuites.FNW_SJLC0021 import Dissolve_Group
from testsuites.FNW_SJLC0022 import End_Task
# from testsuites.FNW_SJLC0023 import Delay_Task
from testsuites.FNW_SJLC0024 import Complete_Task
from testsuites.FNW_SJLC0025 import Stick_Task
from testsuites.FNW_SJLC0026 import Look_Task
from testsuites.FNW_SJLC0027 import Look_Delay_Group
from testsuites.FNW_SJLC0028 import Look_Complete_Group
from testsuites.FNW_SJLC0029 import Look_End_Group
from testsuites.FNW_SJLC0030 import Logout


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '\\test_report\\'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 构建suite
# suite = unittest.TestLoader().discover("testsuites") #获取testsuites下面所有的测试用例
# suite = unittest.TestSuite(unittest.makeSuite(LoginTest))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Look_Card))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Complete_Home_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Delay_Home_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Request_Message))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Long_Stick))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Long_Unstick))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Long_Delete))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Send_message))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Get_Appnames))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Search_Appnames))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Delete_Application))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Add_Application))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Create_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Get_Tasks))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Create_Group))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Look_Group))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Search_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Look_Group_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Search_Group))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Dissolve_Group))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(End_Task))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Delay_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Complete_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Stick_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Look_Task))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Look_Delay_Group))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Look_Complete_Group))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Look_End_Group))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Logout))

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"放牛娃项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)

fp.close()

