for row in range(1,9):
    if row % 2 == 1:
        forRow = "* "
    else:
        forRow = " *"
    for col in range(1,5):
        print(forRow,end="")
    print('\n')
    
