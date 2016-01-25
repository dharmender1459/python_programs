# Write a program to generate a dictionary with given from an integer
n = int(raw_input())
d = dict()
for i in range(1, n):
    d[i] = i+1
print d