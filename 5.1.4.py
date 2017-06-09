from __future__ import division
import numpy as np

q0 =np.array([(1,),(0,)])
q1 =np.array([(0,),(1,)])
                     
def estado(a,b):
    return np.kron(a,b)


#3|01> + 2|11>

print 3*estado(q0,q1)+2*estado(q1,q1)
