def printProfile(me):
    for key,data in me.items():
        print ("My {} is {}".format(key,data))
printProfile({'name' : 'Ana', 'age' : '101', 'country' : 'United States', 'language' : 'Python'})
