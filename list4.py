#List
#index => len-1
#len => index+1

#    0   1   2   3   4   5   6
l1=["a","b","c","d","e","a","b"]
#len 1   2   3   4   5    6  7 

print(l1) #['a', 'b', 'c', 'd', 'e', 'a', 'b']
print()
#          ['a','b','c','d','e','a','b'] 
for x in l1:
    print("list elements are: ",x)

print()
#               7 =>0,1,2,3,4,5,6
for x in range(len(l1)):
    print("list elements are: ",l1[x]) # a /n b /n c /n d /n e /n a /n b