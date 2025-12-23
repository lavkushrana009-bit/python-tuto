#Wap to ask the user to enter names to their 3 favorite movies or  web series and store them in the list.
movies=[]
movies.append(input("Enter the name of your 1st fabourate movies or web  serie name:"))
movies.append(input("Enter the name of your 2nd fabourate movies or web  serie name:"))
movies.append(input("Enter the name of your 3rd fabourate movies or web  serie name:"))
print(movies)


#wapto check ifalistcontains a palindrome of elements.(use copy() method to copy list)
list1=[1,2,1]
print("Original list:",list1)
list2=list1.copy()
print("Copied list:",list2)
if (list2==list1):
    print("list1 contains a palindrome")
else:
    print("list1 does not contains a palindrome")

#Wap to count the number of students with "A" grade in the folllowing tuple
grades_tuple=("c","d","a","a","b","b","a")
print("grades tuple:",grades_tuple)
print(grades_tuple.count("a"))

#store the above value ina list&sort them from "a" to "d"
grades_list=list(grades_tuple)
grades_list.sort()  
print("sorted grades list:",grades_list)