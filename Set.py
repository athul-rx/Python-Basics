#A set is a collection which is unordered, unchangeable*, and unindexed.
#Duplicates are not allowed

thisset = {"apple", "banana", "cherry", "apple"} #curly braces
print(thisset) #only 1 apple will be printed
print(len(thisset)) #length of the set

#Looping through the set, similar to list and tuple
for x in thisset:
  print(x) 

#Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange")
print(thisset) 

#use of update() method- the object can be any iterable(list, tuple, dictionary and set)
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) 

"""Method 	Description
add() -	Adds an element to the set
clear() - Removes all the elements from the set
copy() - Returns a copy of the set
difference() - 	Returns a set containing the difference between two or more sets
difference_update() -	Removes the items in this set that are also included in another, specified set
discard() -	Remove the specified item
intersection() - Returns a set, that is the intersection of two other sets
intersection_update() -	Removes the items in this set that are not present in other, specified set(s)
isdisjoint() - Returns whether two sets have a intersection or not
issubset() - Returns whether another set contains this set or not
issuperset() - Returns whether this set contains another set or not
pop() - Removes an element from the set
remove() - Removes the specified element
symmetric_difference() - Returns a set with the symmetric differences of two sets
symmetric_difference_update() - inserts the symmetric differences from this set and another
union() - Return a set containing the union of sets
update() - Update the set with the union of this set and others"""