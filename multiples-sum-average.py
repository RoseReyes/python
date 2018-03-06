# Print all ODD numbers from 1 to 1000
for x in range(1,1001):
    if x % 2 != 0:
        continue
    print(x)
        

# # Print all multiples of 5 from 5 to 1,000,000
for multiple in range(5,1000000):
    if multiple % 5 != 0:
        continue
    print(multiple)

# # # Prints the sum of all the values in the list
a = [1, 2, 5, 10, 255, 3]
print(sum(a))


# # Prints the average of the values in the list
a = [1, 2, 5, 10, 255, 3]
b = sum(a)/len(a)
print(b)

