import numpy as np

qcero=np.array([(1,),(0,)])
quno =np.array([(0,),(1,)])

def estado(q1,q2):
    return np.kron(q1,q2)

def estados():
    for q1 in [qcero,quno]:
        for q2 in [qcero,quno]:
            yield estado(q1,q2)


def is_unitary(m):
    return np.allclose(np.eye(len(m)), m.dot(m.T.conj()))


def probar_matriz(m):
    print "*"*80
    print m
    print "Es su propia adjunta: %s" % is_unitary(m)
    for e in estados():
        print "Por %s, da %s" % (e.T,np.matmul(m,e).T)

#funcion que intercambia
i=np.array([(0,1,0,0),
            (1,0,0,0),
            (0,0,1,0),
            (0,0,0,1)])
probar_matriz(i)
#funcion constante 0
i=np.array([(1,0,0,0),
            (0,1,0,0),
            (0,0,1,0),
            (0,0,0,1)])
probar_matriz(i)
#funcion constante 1
i=np.array([(0,1,0,0),
            (1,0,0,0),
            (0,0,0,1),
            (0,0,1,0)])
probar_matriz(i)
#funcion identidad
i=np.array([(1,0,0,0),
            (0,1,0,0),
            (0,0,0,1),
            (0,0,1,0)])
probar_matriz(i)
