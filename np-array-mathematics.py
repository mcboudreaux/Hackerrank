import numpy

n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])

a = numpy.zeros((n, m), dtype=int)
b = numpy.zeros((n, m), dtype=int)


for i in range (n):
    x = input().split()
    for j in range(m):
        a[i,j] = x[j] 
        j+=1   
    i+=1

for i in range (n):
    x = input().split()
    for j in range(m):
        b[i,j] = x[j]    
        j+=1   
    i+=1




print (numpy.add(a, b))
print (numpy.subtract(a, b))
print (numpy.multiply(a, b))   
print (numpy.divide(a, b))       
print (numpy.mod(a, b))           
print (numpy.power(a, b))