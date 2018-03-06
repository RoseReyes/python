
'''Find and Replace'''

words = "It's thanksgiving day. It's my birthday,too!"
print(words.find("day"))
newWord = words.replace("day","month")
print (newWord)

'''Min and Max'''
x = [10,54,-90,100,0,-98]
print(max(x))
print(min(x))

'''First and Last'''
x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0],x[7])
newList = [x[0],x[7]]
print(newList)

'''New List'''
originalList = [19,2,54,-2,7,12,98,32,10,-3,6]
originalList.sort()
firstHalf = originalList[:5]
secondHalf = originalList[5:11] 
secondHalf.insert(0,firstHalf)
print(secondHalf)









