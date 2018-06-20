# int
intObj = 1
intObj2 = intObj
intObj2 = 2
intObj == intObj2

# str
strObj = "hey"
strObj2 = strObj
strObj2 = "yoo"

# list
listObj = [1, 2, 3]
listObj2 = listObj
listObj2[1] = 5

# tuple
tupleObj = (1, 2, 3)
tupleObj2 = tupleObj
tupleObj2 += (1, )

# set
setObj = {1, 2, 3}
setObj2 = setObj
setObj2.add(2)

print("int is mutable? ", intObj == intObj2)
print("str is mutable? ", strObj == strObj2)
print("list is mutable? ", listObj == listObj2)
print("tuple is mutable? ", tupleObj == tupleObj2)
print("set is mutable? ", setObj == setObj2)
