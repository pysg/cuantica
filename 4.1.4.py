from __future__ import division
import numpy as np

def normalize(vector):
    return vector/np.linalg.norm(vector)
    
vector = np.array([(3-1j, 2+6j,7-8j,6.3+4.9j,13j,0,21.1)]).T

print vector

print normalize(vector)
