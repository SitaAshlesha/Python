#python list
fruit = ["apples","banana","mango","banana"]
subject = ["science","commerce","Maths"]
fruit.extend(subject)
print(fruit)
print(len(subject))
#list can contain any data type
list1 = ["ggg",445454,True]
print(list1)
fruits = ["apples","banana","mango","cherry"]
print(fruits[-1] )
thislist = ["pen","pencil","paper","earaser","calculator"]
if "pen" in thislist:
    print("yes ,pen is in the list")
else:
    print("no")