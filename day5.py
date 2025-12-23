#Dictionary and sets  
#Dictionary is used for storing data values in key:value pairs.
#they are unorderd, changeable and do notalllowed duplication.

dict={
    "name":"lavkush" ,
    "age":21,
    "cgpa":6.2,
    "marks":[34,45,43],
    "tuple":(1,2,3),
    "set":{1,2,3},
    "dict2":{"a":1,"b":2}

}

print(dict)
print(dict["name"])
print(dict["age"])
print(dict["cgpa"])
print(dict["marks"])
print(type(dict))


#nested dictionary
dict2={
    "student":"lavkush",
    "marks":{
        "real analysis":34,
        "linear alebra":45,
        "topology":43
    }
}

print(dict2)
print(dict2["marks"]["topology"])
  

#Dictionary methords
print(dict2.keys() )     #it will return all the keys of the dictionary
print(dict2.values() )   #it will return all the values of the dictionary
print(dict2.items() )    #it will return all the items of the dictionary in the form of tuples
print(dict2.get("student"))  #it will return the value of the specified key
dict2.update({"age":22})  #it will update the value of the specified key
print(dict2)  
dict2.pop("age")         #it will remove the specified key
print(dict2)
dict2.clear()            #it will remove all the items from the dictionary

#Sets
#Sets are used to store multiple items in a single variable.
#Sets are unordered, unindexed, and do not allow duplicate values.
set1={1,2,3,4,5,5,6,7,8,8}
print(set1)  #it will remove the duplicate values
print(type(set1))
print(len(set1))  #it will return the length of the set
set1=set() #it will create an empty set
print(type(set1))
print(set1)

#Set methords
set2={1,2,3,4,5}
set2.add(6)  #it will add the specified value to the set
print(set2)
set2.remove(3)  #it will remove the specified value from the set
print(set2)
set2.discard(4)  #it will remove the specified value from the set
print(set2)
set2.clear()  #it will remove all the items from the set
print(set2)
set3={1,2,3}
set4={3,4,5}
set5=set3.union(set4)  #it will return a new set that contains all the items from both sets
print(set5)
set6=set3.intersection(set4)  #it will return a new set that contains only the items that are present in both sets
print(set6)
print(set3)
print(set4)

