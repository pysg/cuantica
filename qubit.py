import numpy as np

class Qubit(object):
    def __init__(self,a=1,b=0):
        self.zero = complex(a)
        self.one = complex(b)
        self.__normalize()
        
    def __repr__(self):
        return str(self.zero) + " |0> + " + str(self.one) + " |1>\n"
        
    def h(self):
        """Hadamart gate"""
        a = self.zero + self.one
        b = self.zero - self.one
        return Qubit(a,b)

    def norm(self):
        """Norma"""
        return (abs(self.zero) ** 2 + abs(self.one) ** 2) ** 0.5

    def __normalize(self):
        """Normaliza el vector"""
        norm = self.norm()
        self.zero /= norm
        self.one /= norm

