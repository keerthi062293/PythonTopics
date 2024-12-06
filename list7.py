#List
#append() method is used to add elements to the list.

#    0   1   2   3   4   5   6
l1=["a","b","c","d","e","a","b"]
#len 1   2   3   4   5    6  7 

print("Before adding the values: ",l1) #Before adding the values:  ['a', 'b', 'c', 'd', 'e', 'a', 'b']
print()

#adding data
l1.append('g')

#adding data
l1.append('h')
print("After adding the values: ",l1) #After adding the values:  ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'g', 'h']
print()

#Adding list to the list
l1.append(["h","i","j"])
print("After adding list to list: ",l1) #After adding list to list:  ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'g', 'h', ['h', 'i', 'j']]
print()

#Adding new list to the old list
l2=["k","l","m"]
l1.append(l2)
print("After adding new list to the old list: ",l1) #After adding new list to the old list:  ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'g', 'h', ['h', 'i', 'j'], ['k', 'l', 'm']]
print()

for x in l2:
    l1.append(x) 
print("Adding elements by using 'for' loop: ",l1) # Adding elements by using 'for' loop: ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'g', 'h', ['h', 'i', 'j'], ['k', 'l', 'm'], 'k', 'l', 'm']




