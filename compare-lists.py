list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

for indexOne in range(len(list_one)):
    for indexTwo in range(len(list_two)):
        if len(list_one) != len(list_two):
            print("It's not a match")
            break
        elif type(list_one[indexOne]) == type(list_two[indexTwo]) and (list_one[indexOne] == list_two[indexTwo]):
             print("It's a match!",list_one[indexOne], list_two[indexTwo])
        else: 
            print("values/types does not match",list_one[indexOne], list_two[indexTwo])

