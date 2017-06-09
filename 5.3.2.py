
def toffoli(x,y,z):
    return (x,y,z ^ (x and y))
    
    
def identidad(x,y,z):
    return toffoli(*toffoli(x,y,z))
    

for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            assert identidad(x,y,z) == (x,y,z)
            print x,y,z
