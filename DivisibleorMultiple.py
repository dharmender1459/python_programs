# Write a program which print number between 2000 and 3201 which are divisible of 7 but not a multiple of 5
start, end = input("Enter starting value:"), input("Enter ending value:")
for i in range(start, end):
        if (i % 7== 0 and i % 5!= 0):
                print i,",",

