import unittest
import loginTest

class TestCase_login(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("执行测试工作")

    # def setUp(self) -> None:
    #     print("开始执行测试工作")





    @unittest.skip("该测试用例中断")
    def test_login(self):
        self.assertEqual("登录成功",loginTest.login("admin","123456"))

    def test_login1(self):
        self.assertEqual("登录成功",loginTest.login('admin',' '))

    def test_login2(self):
        self.assertEqual('用户名不能为空',loginTest.login('',''))

suite = unittest.TestSuite()
suite1 = unittest.TestLoader().discover('.',pattern='test*.py')

# list_login = [TestCase_login('test_login'),TestCase_login('test_login1'),TestCase_login('test_login2')]
#
# suite.addTests(list_login)

run = unittest.TextTestRunner(verbosity=2)
# run.run(suite)
run.run(suite1)

