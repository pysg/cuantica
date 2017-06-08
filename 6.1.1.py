import numpy as np

qcero=np.array([(1,),(0,)])
quno =np.array([(0,),(1,)])

def estados():
    for e in [qcero,quno]:
        yield e


def probar_matriz(m):
    print "*"*80
    print m
    for e in estados():
        print "Por %s, da %s" % (e.T,np.matmul(m,e).T)


m = np.array([(1,0),(0,1)])
probar_matriz(m)

m=np.array([(0,1),(1,0)])
probar_matriz(m)

m=np.array([(1,1),(0,0)])
probar_matriz(m)

m=np.array([(0,0),(1,1)])
probar_matriz(m)


