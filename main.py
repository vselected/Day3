# # if, elif and else statements
#
# if True:
#     print("It's True")
#
# if 3>2:
#     print("It's True")
#
# hungry = False
# if hungry:
#     print("Feed me")
# else:
#     print("I'm not hungry")
#
# location = "Somehting"
# if location == "Auto Shop":
#     print("Cars are cool")
# elif location == "Bank":
#     print("Money is cool")
# elif location == "Store":
#     print("Welcome to the store")
# else:
#     print("I don't know much")
#
# name = "Sam"
# if name == "Frankie":
#     print("Hello Frankie")
# elif name == "Sammy":
#     print("Hello Sammy")
# else:
#     print("Hello "+name+", pleasure to meet you")
#
# # For Loops
# mylist = [1,2,3,4,5,6,7,8,9,10]
# for number in mylist:
#     print(number)
#
# mylist = [1,2,3,4,5,6,7,8,9,10]
# for number in mylist:
#     #Check for even
#     if number % 2 == 0:
#         print(number)
#     else:
#         print("Odd number {}".format(number))
#
# list_sum = 0
# for number in mylist:
#     list_sum = list_sum + number
#
# print(list_sum)
#
# string = "Hello World"
# for letter in string:
#     print(letter)
#
# tup = (1,2,3)
# for item in tup:
#     print(item)
#
# my_list = [(1,2), (3,4), (5,6), (7,8)]
# print(len(my_list))
#
# for item in my_list:
#     print(item)
#
# for (a,b) in my_list:
#     print(a)
#     print(b)
#
# d = {"k1":1, "k2":2, "k3":3}
# for key,value in d.items():
#     print(key)
#
# for value in d.values():
#     print(value)
#
# While loops
#
# x = 0
# while x < 5:
#     print("The current value: {}".format(x))
#     x += 1
# else:
#     print("X is not less than 5")
#
# x = [1,2,3,4]
# for i in x:
#     pass
#
# mystring = "Sammy"
# for letter in mystring:
#     if letter == "m":
#         continue
#     print(letter)
#
# mystring = "Sammy"
# for letter in mystring:
#     if letter == "m":
#         break
#     print(letter)
#
# x = 0
# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1

# Useful Operators in Python
#
# my_list = list(range(0,51))
#
# for num in my_list:
#     print(num)
#
# index_count = 0
# for letter in "abcdef":
#     print("At index {} the letter is {}".format(index_count,letter))
#     index_count += 1
#
# word = "abcde"
# for index,letter in enumerate(word):
#     print(index)
#
# my_list = [1,2,3,4,5,6,7,8]
# my_list1 = ["a", "b", "c", "d", "e"]
# for item in zip(my_list, my_list1):
#     print(item)
#
# my_list3 = list(zip(my_list,my_list1))
# print(my_list3)
#
# print("x" in [1,2,3])
# print(2 in [1,2,3])
#
# my_list = [1,10,100]
# print(max(my_list))
# # print(min(my_list))
#
# from random import shuffle
# my_list = [1,2,3,4,5,6,7,8,9,10]
# shuffle(my_list)
# print(my_list)
#
# from random import randint
# print(randint(0,100))
#
#
# result = input("What's your name: ")
# print("Pleasure to meet you {}!".format(result))
#
# # List Comprehensions
# my_string = "hello"
# my_list = []
# for letter in my_string:
#     my_list.append(letter)
#
# print(my_list)
#
# my_list = [letter for letter in my_string]
# print(my_list)
#
# my_list = [num for num in range(0,55) if num%2==0]
# print(my_list)
#
# celcius = [0,10,20,34.5]
# fahrenheit = [((9/5)*temp+32) for temp in celcius]
# print(fahrenheit)
#
# my_string = "Hello"
# print(len(my_string))

# 1) Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this Sentence'
for word in st.split():
    if word[0].lower() == "s":
        print(word)

# 2) Use range() to print all the even numbers from 0 to 10.
mylist = list(range(0,11))
for number in mylist:
    if number % 2==0:
        print(number)

mylist = list(range(0,11,2))
print(mylist)

# 3) Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

