def scoreGrades():
    import random
    random_num = 0
    for index in range(10):
        random_num = random.randint(60,100)
        if random_num == 60 or random_num <= 69:
            print("Score:",random_num,";","Your grade is","-",'D')
        elif random_num == 70 or random_num <= 79:
            print("Score:",random_num,";","Your grade is","-",'C')
        elif random_num == 80 or random_num <= 89:
            print("Score:",random_num,";","Your grade is","-",'B')
        elif random_num == 90 or random_num <= 100:
            print("Score:",random_num,";","Your grade is","-",'A')
    print("End of the program. Bye!")
scoreGrades()
