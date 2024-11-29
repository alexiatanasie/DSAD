import numpy as np
import matplotlib.pyplot as plt

#lambda expressions
mean=lambda a,b: ((a+b)/2)
print(mean(4,6))

#by me
mean=lambda a,b,c,d: ((a+b+c+d)/2)
print(mean(4,6,4,6))

#compute the mean value for a vector
vector_mean =lambda vector: np.mean(vector)
print(vector_mean([1,2,3,4]))

#generator
#generate the squares of the integers from 1 to 10
squares=((x+1)**2 for x in range(10))
print(type(squares),squares)
for square in squares:
    print(square)

#starting for a vector of random values
#create a matrix of (5,7) with values in [1,10)
vect1=np.random.randint(1,10,40)
print(type(vect1),vect1)
for square in squares:
    print(square)

matrix1=np.ndarray(shape=(5,7),buffer=vect1, dtype=int,order='C')
#'C' continuous-populated on the rows
#F Fortran-populated on the columns
#A Any
print(type(matrix1),matrix1)

#get the number of bytes on which an eleemtn of the vector is coded
print(vect1.itemsize)
#skip the first 3 elements of the vector
matrix2=np.ndarray(shape=(5,7),buffer=vect1,dtype=int,order='C',offset=3*vect1.itemsize)
print(matrix2)


#Un dicționar în Python este o structură de date care stochează informații sub formă de perechi cheie-valoare.
# Dicționarele sunt utilizate atunci când dorim să asociem o valoare specifică unei chei și să putem accesa rapid valorile utilizând aceste chei.

#dictionary comprehension
#create a dictionary  with keys and values in [1,10]
dict1={x+1: x+1 for x in range(10)}
print(dict1)

dict1={x+1: x+1 for x in range(13) if (x+1) % 2 == 0} #filtrare pt nr pare , by me
print(dict1)

#create a dictionary with keys such as 'K1','K2',...'K7'(strings)
#and values lists of 5 randomly generated integers in [1,10)

dict2={'K'+str(x+1): [y for y in np.random.randint(1,10,5)] for x in range(7)}
print(dict2)
for(k,v)in dict2.items():
    print(k,':',v)

K=[1,2,3,4,5,6,7]
V=['Stud '+str(x+1) for x in range(7)]
print(V)

#create a dictionary with keys in K and values in V
dict3={k: v for(k,v) in zip(K,V)}
#zip uneste K cu V
#zip(A,B,C) returns a list of tuples (a,b,c)
#with a in A, b in B , c in C
print(dict3)
for(k,v,l)in zip(K,V,['Loc '+str(x+1) for x in range(7)]):
    print(k,',',v,',',l)

#create a dictionary to store the x and y for the function f(x)=(x+1)**2, x in [0,10)
dict4={x+1:(x+1)**2 for x in range(10)}
print(dict4)

#plt.plot(dict4.values()) the parameter is interpreted as being the values for the Y axis
dict5={'X'+str(x+1): (x+1)**2 for x in range(10)}
plt.plot(dict5.keys(),dict5.values())
#the paramteres are : first values for the X axis and secod the values for Y axis
plt.show()

# create a matrix (a bi-dimensional ndarray)
# from a dictionary witch
# has lists of numbers as values
data = {
    'row1': [1, 2, 3],
    'row2': [4, 5, 6],
    'row3': [7, 8, 9]
}
matrix = np.array(list(data.values()))
rows = list(data.keys())

print(matrix)
print(rows)