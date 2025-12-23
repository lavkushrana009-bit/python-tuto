#Wap to store following word meaning in a python dictionary
dict={
    "table":["a piece of furnitune ", "list of facts & figures"],
    "cat":"a samll animal"
}
print(dict)


#you are given a list of subjects for students .
# Assume one classroom is required for 1 subject.
# how many classroom are need by all students
subjects={"python","java","c++","python","javscript","java","python","java","c","c"}
print("Number of classrooms required:",len(subjects))


#wap to enterthe marks of 3 subjects from user and store them in dictionary.
#start with empty dictionary & add one by one. use subject name as key & marks as value
marks_dict={}
marks_dict["C"]=int(input("Enter marks for C: "))
marks_dict["real"]=int(input("Enter marks for real: "))
marks_dict["ADE"]=int(input("Enter marks for ADE: "))
print(marks_dict)

#figure out a way to store 9 & 9.0 as seprate values in set 
#(you can take help of built in data types
my_set={9,9.0,"9"}
print(my_set)