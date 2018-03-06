# #Part 1 - lists firstname and lastname
def names(Students):
    for items in Students:
        print(items['first_name'], items['last_name'])
names(Students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ])

# #Part 2 - Create a program that prints the following format (including number of characters in each combined name):
def studentsInst(users):
    res2 = users['Students']
    print("Students","\n")
    for index, res2 in enumerate(users['Students']):
        print(index+1,"-",res2['first_name'],res2["last_name"],"-",len(res2['first_name'])+len(res2['last_name']))
        print("\n")
        res3 = users['Instructors']
        print("Instructors","\n")
        for index, res3 in enumerate(users['Instructors']):
            print(index+1,"-",res3['first_name'],res3["last_name"],"-",len(res3['first_name'])+len(res3['last_name']))
studentsInst(users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 })

# #Steps in nested dictionaries and list
# #Identify wether the object is a dictionary or a list
# #if it's a dictionary: print the keys. if its a list: print the lenght, print the first item if its of manageable size
# #repeat.
