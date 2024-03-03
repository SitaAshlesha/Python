#Text Type
x = "SITA"
print(type(x))
#Numeric Types int ,float,complex
x = 12
y = 1.2
z = 12j
print(type(x))
print(type(y))
print(type(z))
# Sequence types list,tuple,range
x = ["Raj","rani","sita"]
y = ("bb","hh","hjh")
z = range(6)
print(type(x))
print(type(y))
print(type(z))
#mapping type dict
x = {"name" : "jhon", "age" : 5}
print(type(x))
#set types set and frozen set
x = {"ash","jk","hhh"}
print(type(x))
x = frozenset({"ash","jj","jbn"})
print(type(x))
#boolean type
x = True
print(type(x))
#binary types bytes , bytearray,memoryview
x = b"tia"
print(type(x))
y = bytearray(10)
print(y)
print(type(y))
z = memoryview(bytes(5))
print(z)
print(type(z))
#none type
x = None
print(type(x))

