import numpy as np

print "funcion identidad"
print np.matmul(np.array([(1,0),(0,1)]), np.array([(1,),(0,)]))
print np.matmul(np.array([(1,0),(0,1)]), np.array([(0,),(1,)]))

print "funcion que intercambia"
print np.matmul(np.array([(0,1),(1,0)]), np.array([(1,),(0,)]))
print np.matmul(np.array([(0,1),(1,0)]), np.array([(0,),(1,)]))

print "funcion constante 0"
print np.matmul(np.array([(1,1),(0,0)]), np.array([(1,),(0,)]))
print np.matmul(np.array([(1,1),(0,0)]), np.array([(0,),(1,)]))

print "funcion constante 1"
print np.matmul(np.array([(0,0),(1,1)]), np.array([(1,),(0,)]))
print np.matmul(np.array([(0,0),(1,1)]), np.array([(0,),(1,)]))



