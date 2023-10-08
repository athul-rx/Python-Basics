#A tuple is a collection which is ordered and unchangeable.
#It allows duplicate elements, just like list

#Accessing Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

#Adding a tuple to another tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",) #Single element tuple
thistuple += y
print(thistuple)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) 

#Remove element by converting into list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Looping the tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 