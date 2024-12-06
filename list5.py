#List
#    0   1   2   3   4   5   6
l1=["a","b","c","d","e","a","b"]
#len 1   2   3   4   5    6  7 

print(l1) #['a', 'b', 'c', 'd', 'e', 'a', 'b']
print()

print('a' in l1) #True
print()

if 'a' in l1:
    for x in l1:
        if x=='a':  
            print(x) #a /n a
else:
            print("'a' is not presented in list")