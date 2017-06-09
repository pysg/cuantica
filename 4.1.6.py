from __future__ import division
import numpy as np

vector = np.array([(3j,-2)]).T

def p(index,vector):
    return float(abs(vector[index]**2))/abs(np.linalg.norm(vector)**2)

print p(0,vector)

