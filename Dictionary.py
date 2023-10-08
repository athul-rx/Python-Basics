#Dictionaries are used to store data values in key:value pairs.
#Duplicates are not allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"] #values can be of any type
}
print(thisdict)
print(thisdict["brand"])#value of brand will be printed
thisdict["color"] = "red"

thisdict.update({"color": "black"}) #Update() method
thisdict.pop("model")
print(thisdict)
thisdict.clear() #empty dictionary
del thisdict #to delete the dictionary

#NESTED DICTIONARIES
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily)

"""clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary"""