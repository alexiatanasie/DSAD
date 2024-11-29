import numpy as np
import functions as fun

a=11
b=12
print(a,b)
a,b= fun.swap(a, b)
print(a,b)

#fct parameters passed by object reference
list1=[11,2,1,3,16];
print(type(list1),list1)
fun.listSwap(list1)
print(type(list1), list1)

#generate using COMPREHENSION a list of 100 random val in the interval [-5,5)
vect1=np.random.rand(10)
print(type(vect1),vect1)

vect2 = fun.randomAB(-5, 5, 100) #asa zic eu ca ar fi corect, nu ca el
print(type(vect2),vect2)
list2=[x for x in list(vect2)]
print(type(list2),list2)


#use comprehension with conditions
#extract from list3 the negative odd integeres
list3=[-12,-8,-4,1,4,6,12,13, -7,-1]
list4=[x for x in list3 if x< 0 if x%2==1]
print(list4)

#comprehension with multiple variables
list5=[-4,-6,2,4,5]
list6=[x+y for x in list5 for y in list3]
print(list6)
print(len(list6)) # the number of elements

list7=[x+y for x in list3 for y in list5 if x<0 if x%2==1 if y>0 if y%2==0]
print(list7)

#processing a text file as a list of strings
file_in=open('Functions.py','r')
with file_in as f:
    for line in f:
        print(line[:-1])
        #print(line.strip()) sau mai merge asa :)

#dictionaries
#assoviative data type(k1,v1),(k2,v2)..
#the keys are immutable types
dict1={
    'monday': 3.14,
    'tuesday': 'ale',
    'wednesday' : [1,4,6,7]
}
print(type(dict1),dict1)

#extract the keys of a dictionary
print(type(dict1.keys()),dict1.keys())
print(list(dict1.keys()),type(list(dict1.keys())))

#extract the values of a dictionary
print(type(dict1.values()),dict1.values())

#extract the list pairs of(key,value)
list8=list(dict1.items())
print(type(list8),list8)
#go through the list of pairs
for(k,v) in dict1.items():
    print(k, ':',v)