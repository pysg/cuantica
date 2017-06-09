from __future__ import division
import numpy as np

not_m=np.array([(1,0,0,0),
                (0,1,0,0),
                (0,0,0,1),
                (0,0,1,0)])

print np.matmul(not_m,not_m)
