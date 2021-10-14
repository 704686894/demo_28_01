from HTMLTestRunner import HTMLTestRunner
import loginTest
import unittest

class TestCase_login(unittest.TestCase):

    @unittest.skip("该测试用例中断")
    def test_login(self):
        self.assertEqual("登录成功", loginTest.login("admin", "123456"))


    def test_login1(self):
        self.assertEqual("登录成功", loginTest.login('admin', ' '))


    def test_login2(self):
        self.assertEqual('用户名不能为空', loginTest.login('', ''))


suite = unittest.TestLoader().discover(r'C:\Users\70468\PycharmProjects\untitled',pattern= 'test*.py')

report_test = 'report_test.html'
with open(report_test,'wb') as f:
    runner =HTMLTestRunner(f,title='测试报告',description='v1.0')
    runner.run(suite)