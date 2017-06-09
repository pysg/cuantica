
def toffoli(x,y,z):
    return (x,y,z ^ (x and y))
    
    
def nand(x,y):
    return toffoli(x,y,1)[2]
    

def m_or(x,y):
    return toffoli(toffoli(1,x,y)[2],x,y)[2]
