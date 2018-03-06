
# #Test the data type: If its a string, concatenate it onto a new string. If number add it to a running sum.  
# # If it contains only one type print that type otherwise print "mixed". 
l = ['magical unicorns',19,'hello',98.98,'world']
thisStr = []
total = 0
for mixed in range(0,len(l)):
    if type(l[mixed]) != str and type(l[mixed]) != int and type(l[mixed]) != float:
        print("This is neither string or numbers")
    else:
        print("This is a mixed type")
    if type(l[mixed]) is str:
        thisStr.append(l[mixed])
        print("String:",' '.join(thisStr))  
    elif type(l[mixed]) is int or type(l[mixed]) is float:
        total += l[mixed]
        print("Sum:",total)

# #Traverse through the list and identify string data type. Print all string data type.
l = ['magical','unicorns']
myString = []
for counter in range(len(l)):
    if type(l[counter]) != str:
        print("This is not a string!")
    else: 
        type(l[counter]) is str
        myString.append(l[counter])
print("String:",' '.join(myString))
print("The list you entered is of string type")
 

# #Traverse through the list and identify data type. Sum and print all integers data type.
l = [2,3,1,7,"string",12]
total = 0
for counter in range(0,len(l)):
    if type(l[counter]) != int:
        print("This is not an integer")
    else:
        total += l[counter]
print("The list you entered is of integer type")
print("Sum:",total)
        
        
        
    
