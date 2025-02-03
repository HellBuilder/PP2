mylist = ["apple", "banana", "cherry"]



thislist = ["apple", "banana", "cherry"]
print(thislist)



thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)



thislist = ["apple", "banana", "cherry"]
print(len(thislist))



list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)


list1 = ["abc", 34, True, 40, "male"]

print(list1)



mylist = ["apple", "banana", "cherry"]

print(type(mylist))



thislist = list(("apple", "banana", "cherry"))
print(thislist)



thislist = ["apple", "banana", "cherry"]
print(thislist[1])



thislist = ["apple", "banana", "cherry"]
print(thislist[-1])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.

#Remember that index 0 is the first item, and index 2 is the third



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,




thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)



thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)



thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)



thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) 



thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)



thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist) 



thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)



thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)



thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".



thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)



thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])



thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1



thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)




fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)



newlist = [x for x in range(10)]

print(newlist)



newlist = [x for x in range(10) if x < 5]

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)



thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)



thislist = [100, 50, 65, 82, 23]

thislist.sort(reverse = True)

print(thislist)



def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 



thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)



thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)



list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



"""append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""


