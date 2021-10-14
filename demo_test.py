a, b, c, d = 1, 2, 3, 4
print(a+b-c*d)

sum = 0
for x in range(0, 101, 3):
    sum += x
print(sum)

for x in range(1, 10, 2):
    print(x)

sum_ji = 0
sum_ou = 0
for x in range(0, 101, 3):
    sum_ji += x
for x in range(0, 101, 2):
    sum_ou += x
print(sum_ou - sum_ji)

sum1 = 0
for x in range(0, 101, 1):
    sum1 += x
print(sum1)

n = input("请输入数字：")
n1 = int(n)
if n1 % 3 > 0 or n1 % 5 > 0:
    print("此数不能被3和5整除")
else:
    print("此数可以被3和5整除")

m = input("请输入数字：")
m1 = int(m)
if m1 > 0 and m1 <= 100:
    print(m1)
else:
    print("此数不是1-100以内的数")

x = input("请输入数字：")
y = input("请输入数字：")
z = input("请输入数字：")
x1 = int(x)
y2 = int(y)
z3 = int(z)
list1 = [x1, y2, z3]
list1.sort()
print(list1)

score1 =input("请输入您的成绩：")
score1 = int(score1)
if score1 >= 90 and score1 <= 100 :
    print("A")
elif score1 >= 60 and score1 <= 89:
    print("B")
elif score1 <= 60:
    print("C")
else:
    print("您输入的成绩超出范围")

list2 = ["hello python", "你好", 1, 2]
list3 = list2.copy()
print(list3)