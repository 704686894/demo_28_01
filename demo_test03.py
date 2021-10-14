list1 = [1,2,3,4,5,6,9,8,7,1]
print(list1.count(1))
print(list1.index(7))
list1.append(2)
list1.insert(1,10)
for x in list1:
    print(x)
print(list1.index(10))


list1.pop()
print(list1)
list1.pop()
print(list1)
list1.clear()
list1 = [1,2,3,4,5,6]
list1.remove(1)
print(list1)
list1.reverse()
print(list1)
