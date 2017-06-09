from __future__ import division
import numpy as np

def normalize(vector):
    return vector/np.linalg.norm(vector)
    
a = np.array([(np.sqrt(2)/2, np.sqrt(2)/2)]).T
b = np.array([(np.sqrt(2)/2, -np.sqrt(2)/2)]).T

print np.linalg.norm(a)
print np.linalg.norm(b)

print normalize(a+b)
