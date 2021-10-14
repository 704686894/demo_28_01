# # 求a+aa+aaa+aa的值
# a = input("请输入数字：")
# a = int(a)
# b = input("请输入循环几次")
# b = int(b)
# sum = 0
# temp = 0
# for x in range(b):
#     sum += a
#     a *= 10
#     temp += sum
#
# print(temp)

m = 4
n = 3
for x in range(m):
    xx = 2 * x + 1
    space = int((7 - xx) / 2)
    print(space * ' ' + xx * '*' + space *' ')
for x in range(n):
    xx = 2 * (n - x) - 1
    space = x + 1
    print(space * ' ' + xx * '*' + space * ' ')





#    *
#   ***
#  *****
# *******
#  ******
#   ***
#    *

