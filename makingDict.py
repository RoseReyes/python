def make_dict(list1, list2):
  new_dict = {}
  new_dict = dict(zip(list1,list2)) 
  return new_dict
thisDict = make_dict(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"],["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])
print(thisDict)