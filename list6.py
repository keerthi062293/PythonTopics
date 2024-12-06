#List
#index starts with 0, index= length-1
#length starts with 1, length=index+1
#here range() method is used to it should print the elements given in between the range.

#    0   1   2   3   4   5   6
l1=["a","b","c","d","e","a","b"]
#len 1   2   3   4   5    6  7 

print(l1) #['a', 'b', 'c', 'd', 'e', 'a', 'b']
print()

print(len(l1)) #7
print()
#               7=> 0,1,,2,3,4,5,6
for x in range(len(l1)):
#   print(x) # 0 /n 1 /n 2/n 3/n 4/n 5/n 6
    print()
#   print(l1[x]) # a /n b /n c /n d /n e /n a /n b
    print("index is: " ,x, "value is: ",l1[x])
'''
index is:  0 value is:  a

index is:  1 value is:  b

index is:  2 value is:  c

index is:  3 value is:  d

index is:  4 value is:  e

index is:  5 value is:  a

index is:  6 value is:  b
'''
    