import numpy

vector = numpy.array([5,10,15,20])
matrix = numpy.array([
    [5,10,15],
    [20,25,30],
    [35,40,45]
    ])

print( vector == 10 )
print( matrix == 25 )

row = matrix.sum( axis = 1 )
colum = matrix.sum( axis = 0 )

print( row )
print( colum )




