from __future__ import division
import numpy as np

def is_unitary(m):
    return np.allclose(np.eye(len(m)), m.dot(m.T.conj()))


u1 = np.array([(0,1),
               (1,0)])

u2 = np.array([(np.sqrt(2)/2,np.sqrt(2)/2),
               (np.sqrt(2)/2,-np.sqrt(2)/2)])               

print is_unitary(u1)
print is_unitary(u2)
print is_unitary(np.matmul(u1,u2))
