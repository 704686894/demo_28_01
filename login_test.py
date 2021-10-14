from loginTest import login
from parameterized import parameterized
import unittest

class Test_login1(unittest.TestCase):
    @parameterized.expand([('登录成功','admin','123456'),('用户名不能为空','','123456'),('密码不能为空','admin','')])
    def test_login1(self,expect,username,password):
        self.assertEqual(expect,login(username,password))

