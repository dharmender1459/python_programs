# Write a program that will print the factorial of a number using logic techniques
number = input()
for i in range(number, 1, -1):
    number = number * (i-1)
print (number)


