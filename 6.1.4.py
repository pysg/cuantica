from __future__ import division
import numpy as np

qcero=np.array([(1,),(0,)])
quno =np.array([(0,),(1,)])

hadamard = np.array([(1/np.sqrt(2),1/np.sqrt(2)),
                     (1/np.sqrt(2),-1/np.sqrt(2))])
                     
def estado(q1,q2):
    return np.kron(q1,q2)

def phi2(uf):
    return np.matmul(uf,np.matmul(np.kron(hadamard,np.eye(2)),estado(qcero,qcero)))
    


#funcion que intercambia
uf=np.array([(0,1,0,0),
            (1,0,0,0),
            (0,0,1,0),
            (0,0,0,1)])
print phi2(uf)
#funcion constante 0
uf=np.array([(1,0,0,0),
             (0,1,0,0),
             (0,0,1,0),
             (0,0,0,1)])
print phi2(uf)
#funcion constante 1
uf=np.array([(0,1,0,0),
            (1,0,0,0),
            (0,0,0,1),
            (0,0,1,0)])
print phi2(uf)
#funcion identidad
uf=np.array([(1,0,0,0),
            (0,1,0,0),
            (0,0,0,1),
            (0,0,1,0)])
print phi2(uf)
