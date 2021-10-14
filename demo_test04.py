
for x in range(1,10,1):
   for y in range(x,10,1):
       # print(str(x) + '*' + str(y) + '=' + str(x*y),end=" ")
        print("{} * {} = {}".format((x),(y),(x*y)), end=" ")
   print()

str = input("请输入一些字符")
alpha = 0
dight = 0
space = 0
other = 0
for x in str :
    if x.isalpha():
        alpha += 1
        continue
    elif x.isdigit():
        dight += 1
        continue
    elif x.isspace():
        space += 1
        continue
    else:
        other += 1
print("字母：{alpha},数字：{dight},空白：{space},其他：{other}".format(alpha=alpha,dight = dight,space = space,other=other))

a = input("请输入数字")
s = input("请输入循环几次")
int(s)
list = [y + str(x) for x in range(1,s,1)for y in [a]]
print(list)