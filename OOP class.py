# creating a class
class HumanKind:

    skin = True
    eyes = True
    legs = True
    specie = "mamal"

# creating an object/instance of the class above / 
human_kind_object = HumanKind()
# print(human_kind_object)
# print(human_kind_object.legs)

objects = []
for i in range(10000):
    objects.append(HumanKind())
# print(objects[1005])

from os import name, read
import time, winsound
# class HumanKind:

#     skin = True
#     eyes = True
#     legs = True
#     specie = "mamal"

#     def describe(self):   #Method SELF: points to the current instance of a class
#         print(f"Hello my species is {self.specie}")

#     def  makenoise(self):
#         print("HELLO!!!")
#         winsound.Beep(700,2000)
#         time.sleep(1)
#         winsound.Beep(1000, 500)
#         time.sleep(1)
#         winsound.Beep(3000, 500)

# varname = HumanKind()
# varname.describe()
# varname.makenoise()

#Task: create a class of cat with attributes: name, fur colour, family, and method decribe that prints "hello, I am a cat, my fur colour is {fur colour} and my name is {name}"
# class Cat:
#     name = "Garfield"
#     fur_colour = "Orange"
#     family = "Persian"

#     def describe(self):
#         print(f"Hello, I am a cat, my fur colour is {self.fur_colour} and my name is {self.name}")
# var = Cat()
# var.describe()

# creating a class with instance attributes
# import random
# class Person:
#     species = "Homo Sapien"
#     _class = "Mammal"
#     def __init__(self, name, complexion, height):   #__init__ is initialization, is a magic method that gets executed automatically
#         self.name = name
#         self.complexion = complexion
#         self.height = height
#         self.voice_freq = random.randint(50, 1500)
    # def say_something(self):
#         print(f"Hello, my name is {self.name}.\n I am a {self._class}, and my height is {self.height}")
#         winsound.Beep(self.voice_freq, 500)
#         time.sleep(0.5)
#         winsound.Beep(self.voice_freq, 500)
#         time.sleep(0.5)
#         winsound.Beep(self.voice_freq, 500)

# person1 = Person(name = "Ade", complexion ="Brown skin", height = "5ft9")
# person1.say_something()
# person2 = Person(name = "Segun", complexion = "Dark skin", height = "6ft4")
# person2.say_something()

# class EthnicMeal:
#     def igbo(self):
#         print("Akpu")
#     def yoruba(self):
#         print("Amala")
#     def hausa(self):
#         print("Tuwo Shinkafa")
# meal = EthnicMeal()
# meal.yoruba()

# class Student:
#     def __init__(self, name, gender,age):
#         self.name = name
#         self.gender = gender
#         self.age = age
#     # Accessor instance method
#     def get_name(self): 
#         return self.name
#     def get_gender(self):
#         return self.gender
#     def get_age(self):
#         return self.age
    
#     # Mutator instance method
#     def set_name(self,value):  
#        self.name = value
#     def set_gender(self, value):
#         self.gender = value
#     def set_age(self,value):
#         self.age = value

# stu_one = Student(name = "Kelsey", gender = "Female", age = 17)
# stu_two = Student("Brian", "Male", 35)
# stu_three = Student("Ernie", "Male", 27)
# print(stu_one.get_age())
# stu_one.set_age(13)
# print(stu_one.get_age())

# class School:
#     no_of_students = 0
#     sum_of_scores = 0
    

#     def __init__(self, student_name, student_score):
#         self.student_name = student_name
#         self.student_score = student_score
#         School.add_count()    # OR  self.add_count()
#         School.sum_of_scores += self.get_student_score()
#         # School.no_of_students += 1

#     def get_student_name(self):
#         return self.student_name
#     def get_student_score(self):
#         return self.student_score
    
#     def set_student_name(self, value):
#         self.student_name = value

#     def set_student_score(self, value):
#         self.student_score = value
    
#     @classmethod
#     def add_count(cls):
#         cls.no_of_students += 1

#     @classmethod
#     def average_score(cls):
#         output = cls.sum_of_scores / cls.no_of_students
#         return round(output ,2)


# stud_one = School("Scott", 54.56)
# # stud_one.add_count()
# # print(School.no_of_students)
# stud_two = School("Stylez", 99.00)
# # stud_two.add_count()
# print(School.no_of_students)
# print(School.sum_of_scores)
# print(School.average_score())

# instance_collector = [School("Ifeoma", 64.22), School("Musa", 76.99), School("Bamise", 58.40)]
# print(instance_collector[1].get_student_score())
# print(instance_collector)
# instance_collector.append(School("Raina", 23.34))
# print(instance_collector)
# NOTE: YOU CAN'T USE AN INSTANCE ACTION IN A CLASS METHOD i.e YOU CAN'T USE self. IN A CLASS METHOD
      # BUT YOU CAN USE A CLASS ACTION IN AN INSTANCE METHOD
# print(School.no_of_students)

# write a class that takes in users personal info and write it into a csv file. (Name, Gender, Age, Location), if the user can supply nacme and age correctly then the user should be able to change the location

# import csv
# from csv import writer
# class UserInfo:
    # def __init__(self, name, gender, age, location):
        # self.name = name
        # self.gender = gender
        # self.age = age
        # self.location = location
        # self.user_file()
        # self.set_check(value)
        
    # def user_file(self):
    #     users_file = open("C:/Users/pc/Desktop/Univelcity/UserInfo.csv", mode = "a", encoding = "utf_8", newline = "")
    #     pen = csv.writer(users_file)
    #     pen.writerow(["Name", "Gender", "Age", "Location"])
    #     pen.writerow([self.name, self.gender, self.age, self.location])
    
    # ACCESSOR INSTANCE METHOD
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_location(self):
#         return self.location
    
#    # MUTATOR INSTANCE METHOD
#     def set_location(self, value):
        # self.location = value

    # def set_check(self, value):
    #     check_name = input("Re-enter name here: ")
    #     check_age = input("Re-enter age here: ")
    #     read_file = open("C:/Users/pc/Desktop/Univelcity/UserInfo.csv", mode = "r")
        # read_file = read_file.readlines()
        # stripping = [entry.rstrip("\n") for entry in read_file]
        # stripping = [entry.split(",") for entry in stripping]
        # print(stripping)
        # for item in stripping:
        #     if check_name == item[0] and check_age == item[2]:
        #         item[3] = value
        #         users_file = open("C:/Users/pc/Desktop/Univelcity/UserInfo.csv", mode = "w", encoding = "utf_8", newline = "")
        #         pen = csv.writer(users_file)
        #         pen.writerow(["Name", "Gender", "Age", "Location"])
        #         for entry in stripping:
        #             pen.writerow([entry[0], entry[1],entry[2], entry[3]])




               # self.location = value
               # def change(self):
               # print(self.set_location(input("New location: ")))



# user = UserInfo(input("Input name here: "), input("Input gender here: "), input("Input age here: "), input("Input location here: "))
# print(user)
# print(stripping)
# user.set_check(Sokoto)







# read_file = read_file.readlines()
#         stripping = [entry.rstrip("\n") for entry in read_file]
#         stripping = [entry.split(" ") for entry in stripping]
#         print(stripping)
#         for item in stripping:
#             if check_name == item[0] and check_age == item[2]:
#                 item[3] = value
#                 users_file = open("C:/Users/pc/Desktop/Univelcity/UserInfo.csv", mode = "w", encoding = "utf_8", newline = "")
#                 pen = csv.writer(users_file)
#                 pen.writerow(["Name", "Gender", "Age", "Location"])
#                 for entry in stripping:
#                     pen.writerow([entry[0], entry[1],entry[2], entry[3]])

















