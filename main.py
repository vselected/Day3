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

d = {"k1":1, "k2":2, "k3":3}
for key,value in d.items():
    print(key)

for value in d.values():
    print(value)

# While loops