from __future__ import division
import numpy as np

o1 = np.array([(1,-1j),
               (1j,1)])

o2 = np.array([(2,0),
               (0,4)])               

print (np.matrix(o1) == np.matrix(o1).H).all() #adjunta
print (np.matrix(o2) == np.matrix(o2).H).all() #adjunta

