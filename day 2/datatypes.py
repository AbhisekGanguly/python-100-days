'''
DAY 002 of 100
@author: Abhisek Ganguly
@topic: Datatypes in Python
'''

#DataType

#String
a = 'Abhisek' #it is a string.

#we can find out it's length
print(len(a))

#Strings store each of it's different letter in different memory allocation
print(a[0])

#We can even store numbers as strings.
x = '10'
y = '20'

#When instring format, the numbers doesn't follow ususal mathematical operator.
#If we try to add two numbers in string format:
print(x + y)
#It will just place two string alongside eachother!
#Therefore, for numbers we have other type of datatype!

#Integers
i = 124 #it is an integer
o = 453
print(i + o)
print(i * o)

#In Integers you can normally use all the mathematical tools available and it'll work normal!
#Integers do not take in decimal points which in some cases can be very important for our work.
#for such kind of delicate work, we have another form of datatype

#Float
g = float(5)
#when inputing numbers without decimal, we have to cast it to the variable, like learnt in day 1

h = 9.00
#if decimal is in place while assigning value, then it'll automatically take it as input!
print(g,h)

#You can always convert int/float to str whenever you want to concatinate it with the string.

#Boolean
#It is our final datatype. It holds any of the two predefined value - True or False

z = bool(1) #boolean of 1 is True
l = bool(0) #Boolean of 0 is False
print(z)
print(l)

#It is primarily used for control flow, about which we will soon be learning!