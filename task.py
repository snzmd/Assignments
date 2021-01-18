#!/bin/python

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
op = int(input('Enter option \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division\n'))

if(op==1):
    a = num1 + num2
    print(f'{num1} + {num2} = {a}')

elif(op==2):
    a = num1 - num2
    print(f'{num1} - {num2} = {a}')

elif(op==3):
    a = num1 * num2
    print(f'{num1} * {num2} = {a}')

elif(op==4):
    a = num1 / num2
    print(f'{num1} / {num2} = {a}')

else:
    print("Invalid option")
