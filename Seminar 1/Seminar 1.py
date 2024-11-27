import matplotlib.pyplot as matt
a=5
print(type(a),a)
a='ale kook'
print(type(a),a)

'''aleeee'''
a=8
b=6
print(a//b)
#the rest of a division
print(a%b)
#the power operator
print(a**b)

string1='ale'
print(type(string1),string1,id(string1))
string1+='tenerife' #string concatenation
print(type(string1),string1,id(string1))
string_2 = 'ale said: "tenerife!"'
print(string_2)
string_3 = '''alexis said: "tenerife trip"'''  # a triplet of apostrophes
print(string_3)

#lists
list1=[1,3.14,'ale',[3,4,6]]
print(type(list1),list1)

#list slicing
list3=[0,1,2,3,4,5,6,7,8,9]
print(list3)
print(list3[:])
print(list3[::])

#substract the elements with even index
print(list3[::2])

#substract the elements with odd index
print(list3[1::2])

#the last element of the list
print(list3[-1])

#reverrse the elements of the list
print(list3[-1::-1])
print(list3[::-1])

#list comprehension
list4=[x for x in list3]
print(list4)


list5=[x for x in range(0,100,1)]
print(list5)
list5=[(x+1) for x in range(100)]
print(list5)

list2=[((x+1)**2)for x in range (50)]
print(list2)

matt.plot(list5)
matt.plot(list2)
matt.plot(list3)

matt.show()