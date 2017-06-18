#!/usr/bin/python

x = 0

while x < 15:
	print ('x is currently: ', x)
	print ('x is still less than 10: , adding 1 to x')
	x = x + 1

	if x == 9:
	    print ('x is equal to 9')
         
            print("condition satisfied so exiting")
            break
	else:
	    print ('continuing')
	    continue 
