#!/usr/bin/python

l = [[1,2] , [3,5,6,7] , [4,6,7,9]]

count = 1
for i in l:
    print("sublist: ", i)
    if i == [1,2]:
 	 print("testing pass")
         pass
	 print("hello pass")
	 count = count + 1
    elif i == [3,5,6,7]:	
	 print('testing ocntinue')
         continue
      	 count = count + 1
	 print('Hello continue')
    elif i == [4,6,7,9]:
         print("matched the if consition")
	 print(count)
