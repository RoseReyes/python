def greaterY(arr,Y):
    count = 0
    for index in range(0,len(arr)):
        if arr[index] > Y:
            count += 1
        print(count)
greaterY([1,2,4,5],3)

def print