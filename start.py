# temperature = 50
# if temperature < 20:
#     print("This is a hot day")
# elif temperature > 20:
#     print("this is a cold day")
# else :
#     print("have a wonderful day")
# print("0----")
# print(" ||||")
# print('---' * 40)
# def greet(name):
#     print("Hello " + name)
#
# greet("Sarah")
# ceej = 40
# ceej = 60
# print(ceej)
# name = 'john smaith'
# age = 20
# is_new = True
# depart = input('what is your department? ')
# print('your department is ' + depart)
# name = input('what is your name? ')
# colour = input('what is you colur? ')
# print(name + ' likes ' + colour)
# dob = input('enter your year of birth? ')
# current = input('enter the current year? ')
# your_date_birth = int(current) - int(dob)
# print(your_date_birth)
# weight_pounds = input('what is your weight? ')
# converted = int(weight_pounds) * 0.45
# print(converted)
# course = ("hello 'world'")
# print(course[:])
# first = 'jogn'
# last = 'smith'
# message = first + '[' + last + ']' 'is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg)
# course = ("hello 'world'")
# # print(course.replace('hello', 'morning'))
# print('hello' in course)
# x = 10 * 5 * 5 ** 5
# print(x)
# y = (2+22) * 23 * 22
# print(y)
import math
from random import randint

from dbt.cli.params import output

# temperature = 60
# if temperature < 30:
#     print('it is a hot day')
# elif temperature > 30:
#     print('it is a cold day')
# else:
#     print('have a wonderful day')
# is_hot = False
# is_cold = True
# if is_hot:
#     print('it is a hot day')
# elif is_cold:
#     print('is is a cold day wear clothe ewu')
#     print('fowl')
# else:
#     print('enjoy your fowl')
# house = 1000000
# has_credit = True
# if has_credit:
#     down_payment = 0.1 * house
# else:
#     down_payment = 0.2 * house
# print(f"down payment: {down_payment}")
# phone = 200000
# is_good = True
# if is_good:
#     down_payment = 0.2 * phone
# else:
#     down_payment = 0.3 *phone
# print(f"pay now is : ${down_payment}")
# high_income = True
# criminal_record  = False
# if high_income and criminal_record:
#     print('your are eligible')
# temperature = 50
# if temperature < 30:
#     print("the temperature is less than 30 and it is cold")
# elif temperature > 30:
#     print("it a hot day")
# else:
#     print("it is not hot or cold at all")
# name = "ffd"
# if len(name) < 3:
#     print("please this name is not valid")
# elif len(name) > 50:
#     print("the name is to much kilode")
# else:
#     print("names looks good")
# weight = int(input('enter your weight  '))
# unit = input('(L)bs or (K)g ')
# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f"you are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"you are {converted} pounds")
# x = 1
# while x <= 40:
#     print('*' * x)
#     x = x + 1
# print("done")
# secret_number = 9
# count_guess = 0
# guess_limit = 3
# while count_guess < guess_limit:
#     guess = int(input('Guess: '))
#     count_guess += 1
#     if guess == secret_number:
#         print('you have won')
#         break
# else:
#     print('you have failed')
# command = ""
# started = False
# while command != "exit":
#     command = input('> ').lower()
#     if command == "start":
#         if started :
#             print("car already started ")
#         else:
#             started = True
#             print("Car has started")
#     elif command == "stop":
#         if not started:
#             print("car already stopped")
#         else:
#             started = False
#             print("car has stopped")
#     elif command == "help":
#         print("""
# type START to start
# type STOP to stop
# type HELP to see command
#         """)
#     elif command == "exit":
#         break
#     else:
#         print("invalid command")
# for item in range(9, 20, 2):
#     print(item)
# prices = [10, 20, 30, 40]
# total = 0
# for price in prices:
#     total += price
# print(f'the total is {total }')
# for x in range(4):
#     for y in range(3):
#         print(f'{x}, {y}')
# numbers = [2,2,2,2,5]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#         print(output)
# names = ['john', 'fowl', 'ewu']
# print(names[2])
# numbers = [2,4,5,6,7,1,10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)
# numbers = [2,5,3,9,1]
# numbers.insert(2,33)
# print(numbers)
# numbers = [2,5,3,9,1]
# print(numbers.index(9))
# numbers = [2,5,3,9,1,9,9]
# print(numbers.count(9))
# numbers = [2,5,3,9,1,9,9]
# numbers2 = numbers.copy()
# numbers.append(40)
# print(numbers2)
# numbers = [4,4,6,3,7,4,9]
# original = []
# for number in numbers:
#     if number not in original:
#         original.append(number)
# print(original)
# numbers = (11,2,4,6)
# print(numbers[2])
# numbers = (11,2,4,6)
# m,r,u,r = numbers
# print(u)
# customer = {
#     "names": "john smith",
#     "age": 10,
#     "verified": True
# }
# # customer["names"] = "Jack ewu"
# customer["hired"] = False
# print(customer["hired"])
# phone = input("phone number: ")
# keys = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }
# output = ""
# for key in phone:
#     output += keys.get(key, "none") + " "
# print(output)
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)" : "😂",
#     ":(" : "😢"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word)
# print(output)
# def greet_fowl(first_name, last_name):
#     print(f'heillo there {first_name} {last_name}')
#     print('welcoome')
# print("start")
# greet_fowl("john", "sammy")
# greet_fowl("mary", "ewu")
# print("fowl")
# def greet_fowl(first_name, last_name):
#     print(f'heillo there {first_name} {last_name}')
#     print('welcoome')
#  print("start")
#  greet_fowl("john", "sammy")
#  greet_fowl("mary", "ewu")
#  calc_cost(shipping=20, cost=100, discount=0.2)
#  print("fowl")
# def square(number):
#     return number * number
# # result = square(3)
# print(square(3))
# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😂",
#         ":(": "😢"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word)
#         return output
# message = input(">")
# print(emoji_converter(message))
# try:
#     age = int(input("enter: "))
#     incoome = 20000
#     risk = age/incoome
#     print(age)
# except ZeroDivisionError:
#     print("age can not be zero")
# except Value Error:
#     print("invalid value")
# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
# point = point(10,20)
# print(point.x)
# class mamal:
#     def walk(self):
#         print("walk")
# class Dog(mamal):
#     pass
# class Cat(mamal):
#     pass
# dog1 = Dog()
# dog1.walk()
# import converter
# from converter import kg_to_lbs
# print(converter.kg_to_lbs(70))

# from utils import find_max
# numbers = [10, 3, 6, 2]
# max = find_max(numbers)
# print(max)
# import eccommerce1.shipping
# eccommerce1.shipping.calc_shipping()
#import random
# for i in range(3):
#     print(random,randint(5, 100))
# members = ['jdd', 'ekekeoe', 'oekeke', 'oeekwk']
# leader = random.choice(members)
# print(leader)
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
# dice = Dice()
# print(dice.roll())
from pathlib import Path
# path = Path("eccommerce1")
# print(path.exists())
# path = Path("emails")
# print(path.rmdir())
path = Path()
# for file in (path.glob('*.py')):
#     print(file)
for file in (path.glob('*')):
    print(file)

