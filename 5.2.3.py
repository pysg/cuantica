from __future__ import division
import numpy as np

mnot=np.array([(0,1),
               (1,0)])
mor =np.array([(1,0,0,0),
               (0,1,1,1)])

print np.matmul(mnot,mor)
