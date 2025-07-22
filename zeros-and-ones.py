
# You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

# Input Format

# A single line containing the space-separated integers.

# Constraints


# Output Format

# First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

# Sample Input 0

# 3 3 3
# Sample Output 0

# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]
# [[[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]]
# Explanation 0

# Print the array built using numpy.zeros and numpy.ones tools and you get the result as shown.


import numpy 

def get_y(med):
    return int(med[3]) 

def get_x(med):
    return int(med[2]) 

def get_n(med):
    return int(med[1])

def get_m(med):
    return int(med[0])
    

med = input("Numero: ").split() 
tam = len(med)

if tam == 4:
    print(numpy.zeros((get_m(med), get_n(med),get_x(med),get_y(med)), dtype=int))
    print(numpy.ones((get_m(med), get_n(med),get_x(med),get_y(med)), dtype=int))  

if tam == 3:
    print(numpy.zeros((get_m(med), get_n(med),get_x(med)), dtype=int))
    print(numpy.ones((get_m(med), get_n(med),get_x(med)), dtype=int))  
    
if tam == 2:
    print(numpy.zeros((get_m(med), get_n(med)), dtype=int))
    print(numpy.ones((get_m(med), get_n(med)), dtype=int))
    
if tam == 1:
    print(numpy.zeros((get_m(med)), dtype=int))
    print(numpy.ones((get_m(med)), dtype=int))    