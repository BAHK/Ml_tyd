import numpy as np
from numpy import pi

print( np.arange( 15 ))
a = np.arange( 15 ).reshape( 3,5 )
print( "a = ")
print( a )

print( "a.shape is")
print( a.shape )
print( "a's dimesion is : ")
print( a.ndim )
print( "a.dtype.name is : ")
print( a.dtype.name )


zero = np.zeros((3,2))
one = np.ones((2,3,4), dtype = np.int32 )
print( zero )
print( one )
print( one.ndim )


aa = np.arange(10,30,5)
print( aa )

bb = np.random.random((2,3))
print( bb )


a = np.array( [ 20, 30, 40, 50 ])
b = np.arange( 4 )
print( a )
print( b )
c = a - b 
print( c ) 


print("============ Matrix product ===========")

A = np.array([
    [1,1],
    [0,1]
    ])

B = np.array([
    [2,0],
    [3,4]
    ])

print("----- A -----")
print( A )


print("----- B -----")
print( B )


print("----- A * B-----")
print( A*B )


print("----- A.dot( B )-----")
print( A*B )
print("----- A * B-----")
print( np.dot( A, B ))












