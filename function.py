import numpy as np
# defining a function
def computeNumbers(a, b, c):
    sum_nos = a + b + c

    return sum_nos

print(computeNumbers(3, 5, 8))

using the lambda function
multiply_numbers = lambda x, y : x + y
print(multiply_numbers(2,5))

function in function
f = max
print(f([2,3,6,8]))

Write a function my_checker_board(n) where the output m is an n×n array with the following form
m = ([[1, 0, 1, 0, 1 ]
    [0, 1, 0, 1, 0 ]
    {1, 0, 1, 0, 1 }
    [0, 1, 0, 1, 0]
    [1, 0, 1, 0, 1]])

# What is the sum of every integer from 1 to 3
# firt define an initial sum value/counter
counter = 0
for i in range(1,4):
    counter = counter + i
print (counter)

# List Comprehension
# If x = range(5), square each number in x, and store it in a list y
# If we do not use list comprehension, the code will look something like this:
x = range(5) 
y = []
for i in x: 
    y.append(i**2) 
print(y)
output - [0, 1, 4, 9, 16]

# If we use list comprehension, the code will look something like this:
y = [i**2 for i in x] 
print(y)
output - [0, 1, 4, 9, 16]

x = [j + 2 for i in q]
print(x)