import unittest, time
import os, sys

sys.path.append(os.getcwd())
from common.HTMLTestRunner import HTMLTestRunner
# from scripts.test_partnershow import Test_PartnerShow
from scripts.test_login import Test_login

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
        HTMLTestRunner(stream=f, title='PAI_daodangui', description='win10', verbosity=2).run(discover)
    f.close()
