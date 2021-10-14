# print(1+1);
# print(type("你好啊"));
# print(type(123));
# print(type(3>2));
# print(type(2>3));
# print(type(0.2));
# a=2;
# b=3;
# c=4;
# e = a + b + c;
# print(e);
# print(b //2)
# print(a ** 2)
# print(3 % 5)
tp = tuple()
tp1 = ()
tp2 = (1,2,3,4,5,6,7,8,9,8,7,6,5)
print(tp)
print(tp1)
print(tp2)
dt = {}
dt1 = dict()
dt2 = {'a':'hello','b':'world'}
print(dt)
print(dt1)
print(dt2)
print(dt2['a'])
print(dt2.get('a'))
# print(dt2.items())
for x in dt2.items():
    print(x,end=" ")

for x in dt2.keys():
    print(x, end=" ")

print(dt2.values())
dt2.pop('b')
print(dt2)
dt2.setdefault('b')
print(dt2)
dt2.popitem()
print(dt2)
dt3 = {'c':'你好','d':'不好'}
dt2.update(dt3)
print(dt2)
s1 = "我的名字叫'%s'"%'张三'
print(s1)

s2 = "我买了%d斤菜"%100
print(s2)
s3 = '我花了%+8.2f元买了iphone13'%-139800
print(s3)

print("今天星期{}，张三买了{}元菜".format('7',100))
print("我是位置参数,{0} {1}".format('java','c++'))
print("我是关键字参数:{x},java".format(x='hello'))
str1 = "abcdefghhijklmnabcdefghijklmn"
print('.'.join(str1))
print(str1.split('m'))
print(str1.find('m',0,20))
print(len(str1))
print(str1.startswith('a',0,10))
print(str1.endswith('n',0,10))

print(str1.replace('a','w'))
str4 = '123456789'
print(str4.isdigit())
str5 = 'sadasdasda123456'
print(str5.isalpha())
str6 = '   dasdaas    '
print(str6.strip())
print(str6.upper())
print(str6.lower())
lst = [1,2,3,4,5,6,7,8,9,10]
print('取出第二个至第八个的数字:',lst[1:9:1])
print('取出第二个至第八个的数字:',lst[:10:3])
