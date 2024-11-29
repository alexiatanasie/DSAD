import numpy as np
from numpy.f2py.rules import aux_rules
def swap(a,b):
     aux=a
     a=b
     b=aux
     #print(a,b) #nu face swap
     return a,b

def listSwap(l):
     aux=l[0]
     l[0]=l[1]
     l[1]=aux  #no return needed, lists are mutable

def randomAB(a,b,n):
     return a+np.random.rand(n)*(b-a) # a vector is multiplied with scalar on the right

