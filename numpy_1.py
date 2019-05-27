import numpy

world_alcohol = numpy.genfromtxt("world_alcohol.txt",delimiter = ",",dtype = str)
print(type(world_alcohol))
print(world_alcohol)
#print(help(numpy.genfromtxt))

vector = numpy.array([5,10,25,20])
matrix = numpy.array([[11,12,13],[21,22,23],[31,32,33]])
third_country = world_alcohol[2,2]

print( vector )
print( matrix )

print( vector.shape )
print( matrix.shape )
print( third_country )
print( vector[0:3])
print( matrix[:,2])

print( "=================")
print( matrix[:,0:2])
print( "=================")
numbers = numpy.array([1,2,3,4])
print( numbers )
print( numbers.dtype)


