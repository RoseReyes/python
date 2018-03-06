# #Part 1: Create a function called draw_stars() that takes a list of numbers and prints out *.
# def draw_stars(arr):
#     for index in range(0,len(arr)):
#         arr[index] = ("*") * arr[index]
#         print(arr[index])
# draw_stars([4,6,1,3,5,7,25])

#Part 2: Allow a list containing integers and strings to be passed to the draw_stars()function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below
def draw_stars(arr):
    for index in range(0,len(arr)):
        if type(arr[index]) is int:
            arr[index] = ("*") * arr[index]
            print(arr[index])
        else:
            print(arr[index][0].lower()*len(arr[index]))   
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

