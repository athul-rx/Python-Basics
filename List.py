list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 
#append() method is use to combine lists. This method is similar to extend() method.


#changing the range of elements in the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#list Comprehension, if we want to create a new list based on the existing list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) 

#sort a list
number = [100, 50, 65, 82, 23]
number.sort()
print(number)
#sorting in descending order
number.sort(reverse=True)
print(number)

#reverse the order of elements
fruit = ["banana", "Orange", "Kiwi", "cherry"]
fruit.reverse()
print(fruit)

#Method -	Description
#append() -	Adds an element at the end of the list
#clear() -	Removes all the elements from the list
#copy() -	Returns a copy of the list
#count() -	Returns the number of elements with the specified value
#extend() -	Add the elements of a list (or any iterable), to the end of the current list
#index() -	Returns the index of the first element with the specified value
#insert()	- Adds an element at the specified position
#pop() -	Removes the element at the specified position
#remove() -	Removes the item with the specified value
#reverse() -	Reverses the order of the list
#sort() -	Sorts the list