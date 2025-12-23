# list in python  is mutable and can bechanged,
#a built in datatype that stores set of values
#it can store element of different datatypes( int,float ,string etc)
#list is defined using square brackets []
marks=[90,85,70,80,40]
print(marks)
print(type(marks))
print(marks[1])#85

students=["lavkush",2,"delhi"]
print(students)
students[0]="Rana"#allowing to change value
print(students)
print(len(marks))

#list slicing
print(marks[1:3])
print(students[:2])
print(students[1:])
print(marks[-3:-1])

#list methods
#append() method to add element at end of list
marks.append(95)
print(marks)
marks.sort()#sort the list in ascending order
print(marks)
marks.sort(reverse=True)#sort the list in descending order
print(marks)
marks.reverse()
print(marks)
marks.insert(3,34)#insert 34 at index 3
print(marks)
marks.remove(95)#remove 95 from list
print(marks)
marks.pop()#remove last element from list
print(marks)


#tupple in python is immutable and can't be changed
#a built in datatype that stores set of values
tup=(2,3,4,5,6)
print(tup)
print(type(tup))


# tuple methods
print(tup.count(3))#return count of given element in tuple
print(tup.index(5))#return index of given element in tuple