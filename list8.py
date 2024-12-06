#List 
#insert() method is used to insert the in particular space and it will take the 2 aruguments, 1. index position 2. insertion value

#    0   1   2   3   4   5   6
l1=["a","b","c","d","e","a","b"]
#len 1   2   3   4   5    6  7 
print(l1) #['a', 'b', 'c', 'd', 'e', 'a', 'b']
print()

l1.insert(6,"f")
print(l1) #['a', 'b', 'c', 'd', 'e', 'a', 'f', 'b']
print()

l1.insert("h")
print(l1) #TypeError: insert expected 2 arguments, got 1 because here we are not mentioning the index value
print()


