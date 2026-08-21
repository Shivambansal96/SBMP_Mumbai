


# # # class NegativeNumberError():
# # #     pass

# # # # try:
# # # #     num = int(input("Enter a num: "))

# # # #     if(num < 0):
# # # #         raise NegativeNumberError("Number is Negative !!!")

# # # #     print(f"Number = {num}")

# # # # except:
# # # #     print("Error")




    
# # # # try:
# # # #     num = int(input("Enter a num: "))

# # # #     if(num < 0):
# # # #         raise NegativeNumberError("Number is Negative !!!")

# # # #     print(f"Number = {num}")

# # # # except Exception as e:
# # # #     print(f"Error = {e}")


# # # try:
# # #     print(1)

# # #     if(99):
# # #         raise NegativeNumberError

# # #     print(3)

# # # except:
# # #     print("Error")

# # # finally:
# # #     print("Code ENds")


# # def multiplyBy2(x):
# #     return x * 2

# # arr = [4, 5, 7, 2, 6]
# # res = list(map(multiplyBy2, arr))

# # print(res)




# # # ------------------------------------------------------------------ #

# # class Student:
# #     name = "Shivam Bansal"
# #     marks = 98

# #     def __init__(self):
# #         print(f"INSIDE = {self}")
# #         # print("Student Object Created !")

# # s1 = Student()  # Creating an Object
# # print(f"OUTSIDE = {s1}")
# # # print(s1.marks)

# # print("----------------------------------")

# # s2 = Student()
# # print(f"OUTSIDE = {s2}")





# # ------------------------------------------------------------------ #

# class Student:
#     clgName = "SBMP"
#     training = "Python Basic to OOPS"

#     def __init__(self, fullName, age, rollNo):
#         self.name = fullName
#         self.age = age
#         self.rollNo = rollNo

#     def hello(self):
#         print(f"Welcome Student")

# s1 = Student("Shivam Bansal", 27, 16)  # Creating an Object
# # print(s1.name)
# s1.hello()

# # s2 = Student("Shiva")  # Creating an Object
# # print(s2.name)


import math

class Circle:

    def __init__(self, radius):
        self.r = radius

    def area(self):
        print(f"Area of Circle with radius {self.r} = {(math.pi* self.r * self. r):.2f}")

    def perimeter(self):
        print(f"Perimeter of Circle with radius {self.r} = {(math.pi* 2 * self. r):.2f}")

c1 = Circle(int(input("Enter radius for Circle 1: ")))
c2 = Circle(int(input("Enter radius for Circle 2: ")))

c1.area()
c1.perimeter()

print("=========================================")

c2.area()
c2.perimeter()
