# 要求 ： 通过面向对象实现一个简易版的学生管理系统，要求功能中有增、删、改、查功能
# ，具体数据可以定义在一个字典中 ，若增加，将数据插入字典 ，若删除 ，将数据从字典中删除，依次类推

class students():

    dict_stu = {'姓名':"", '性别':"",'年纪':""}


    def update(self,name,sex,grade):
        self.dict_stu['性别'] = sex
        self.dict_stu['姓名'] = name
        self.dict_stu['年纪'] = grade







st1 = students()

st1.update('张三','男','二年级')
st1.update('李四','女','三年级')
st1.dict_stu.values()
for x in st1.dict_stu.values():
    print(x,end=" ")