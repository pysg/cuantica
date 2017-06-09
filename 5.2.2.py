from __future__ import division
import numpy as np

q0 =np.array([(1,),(0,)])
q1 =np.array([(0,),(1,)])
                     
def estado(a,b):
    return np.kron(a,b)


mor =np.array([(1,0,0,0),
               (0,1,1,1)])

print np.matmul(mor,estado(q0,q0))
print np.matmul(mor,estado(q0,q1))
print np.matmul(mor,estado(q1,q0))
print np.matmul(mor,estado(q1,q1))
