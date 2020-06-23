import unittest, time
import os, sys

sys.path.append(os.getcwd())
from scripts.test_partnershow import Test_PartnerShow
from scripts.test_login import Test_login
from common.HTMLTestRunner import HTMLTestRunner
from common.send_email import SendEmail


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Test_login('test_login'))
    # suite.addTest(Test_PartnerShow('test_show'))
    # 简写
    # suite = [Test_PartnerShow('test_show'), Test_PartnerShow('test_show')]
    # unittest.TextTestRunner().run(suite)

    discover = unittest.defaultTestLoader.discover("./scripts/", pattern="test*.py")

    dir_path = "./report/"
    nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
    report_name = dir_path + nowtime + "report.html"
    with open(report_name, 'wb') as f:
        HTMLTestRunner(stream=f, title='PAI_daodangui', description='win10，Python3', verbosity=2).run(discover)
    f.close()

    user_list = ['zhilei@llzey.com']
    sub = "接口自动化测试"
    content = "倒蛋鬼接口测试报告"
    SendEmail().send_email(user_list, sub, content, report_name)
