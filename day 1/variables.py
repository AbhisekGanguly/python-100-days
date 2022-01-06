'''
DAY 001 of 100
@author: Abhisek Ganguly
@topic: Variables in python.
'''

#variables are a way to assign and store data.
#creating a varibale in python has no command for it.
#a variable is created as soon as you assign a value to it.

a = 5 #this is a variable containing number
x = "Abhisek" #this is a variable containing my name in programming we call it string

#we can now ask for this varibales anywhere in the program and it'll show up right there!
#here we are calling the variables using print function and printing it!
print(x)
print(a)

#variables in python doesn't need to be declared with any specific type.
#python can decide and automatically assign type to the variables.
#you can check the type of variables with the type function\
print(type(a))
print(type(x))

#Casting: If you want a specif type of variable, you can make it possible using casting.
name = str("Abhisek")
height = float(6.3)

#variables are case sensitives, i.e. A is not the same as a
A = 10
print(A, a)
# here A = 10 and a = 5