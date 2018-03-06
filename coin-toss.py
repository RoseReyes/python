import random
x = .23945593
y = .798839238
headcount = round(x)
tailcount = round(y)
tossresult = random.choice(['head','tail'])
print("Starting the program")
for index in range(5000):
    if tossresult == "head":
        headcount += 1
        print("Attempt#",index,":","Throwing a coin...","It's a",tossresult,"!...","Got",headcount,"head(s) so far and",tailcount,"tails(s) so far")
    elif tossresult == "tail":
        tailcount +=1
        print("Attempt#",index,":","Throwing a coin...","It's a",tossresult,"!...","Got",headcount,"head(s) so far and",tailcount,"tails(s) so far")
print("Ending the program, thank you!")
            
 #need to refactor the code   
    
        
