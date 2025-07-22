import numpy
numpy.set_printoptions(legacy='1.13')



entrada= input().split()
print (entrada[0])
print (entrada[1])
print (entrada[2])

array = numpy.zeros((len(entrada)), dtype=float)

for i in range((len(entrada))):
    array[i] = float(entrada[i])
    i+=1

print(array[0] )
print(entrada[0])
print(array[1] )
print(entrada[1])
print(array[2] )
print(entrada[2])

print (numpy.floor(array))
print (numpy.ceil(array))         
print (numpy.rint(array))  