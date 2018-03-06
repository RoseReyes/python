# #Print 1 to 2000 and determine if its an odd/even number
def odd_Even(numIdx,number):
    for numIdx in range(numIdx,number):
        if numIdx % 2 != 0:
            print("Number is:",numIdx,"The number is an odd number.")
        else: 
            print("Number is:",numIdx,"The number is an even number.")
odd_Even(1,2001)

# #Create a function called 'multiply' that iterates through each value in a list and returns a list where each value has been multiplied by 5.
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print (b)

#Hacker Challenge- Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a two-dimensional list. 
# Each internal list should contain the 1's times the number in the original list.

def layered_multiples(arr,num):
    import numpy as np
    new_array = []
    for index in range(len(arr)):
        arr[index] *= num
        new_array.append(np.ones((arr[index]),dtype = np.int))
    return new_array
x = layered_multiples([2,4,5],3)
print (x)