# # # # ## INHERITANCE # # # # ## 

# # # class Shape:
# # #     sides = "No idea"

# # # class Triangle(Shape):
# # #     # sides = 3
# # #     demo = "checking"

# # # class RightAngledTriangle(Triangle):
# # #     abc = "abc"

# # # class Isosceles(Triangle):
# # #     defg = "abcdefg"

# # # t1 = Triangle()
# # # print(t1.sides)

# # # r1 = RightAngledTriangle()
# # # print(r1.sides)

# # # i1 = Isosceles()
# # # print(i1.defg)


# # # # ## INHERITANCE Practice Question (using super method) # # # # ## 

# # class Employee:

# #     def __init__(self, role, dept, salary):
# #         self.role = role
# #         self.department = dept
# #         self.salary = salary

# #     def showDetails(self):
# #         print(f"Role: {self.role}")
# #         print(f"Department: {self.department}")
# #         print(f"Salary: {self.salary}")


# # # e1 = Employee("Technical Trainer", "IT", 100000)
# # # e1.showDetails()

# # print()
# # print("------------------------------------------")
# # print()


# # class Engineer(Employee):

# #     def __init__(self, name, age, role, dept, salary):
# #         self.name = name
# #         self.age = age
# #         super().__init__(role, dept, salary)
# #         # Employee().__init__() 

# #     def showDetails(self):
# #         print(f"Name: {self.name}")
# #         print(f"Age: {self.age}")
# #         super().showDetails()
# #         # Employee().showDetails()

# # # eng1 = Engineer("Shivam", 27, "TT", "CSE", 99000)
# # # eng1.showDetails()



# # # # # ## Abstraction # # # # ## 

# # from abc import ABC, abstractmethod

# # class Animal(ABC):

# #     @abstractmethod
# #     def sound():
# #         pass

# # class Dog(Animal):
# #     def sound(self):
# #         print("Dog Barks !")

# #     def food(self):
# #         print("Eats Pedigree !")


# # class Cat(Animal):
# #     # def sound(self):
# #     #     print("Cat Meows !")
# #     pass

# # # a1 = Animal()

# # # d1 = Dog()
# # # d1.sound()

# # c1 = Cat()
# # # c1.sound()



# # # # # Encapsulation # # # # 

# class Student:
#     def __init__(self, name):
#         self.name = name

#     # def welcomeMsg(self):
#     #     print(f"Welcome {self.name}")

#     # @staticmethod
#     def welcomeMsg(self):
#         print(f"Welcome Student")

#     # def teacherName(self):
#     #     print(f"Teacher = {self.name}")

# s1 = Student("Shivam")
# # s1.teacherName()
# s1.welcomeMsg()


# class Account:

#     def __init__(self, accNo, accPass):
#         self.accNo = accNo
#         self.__accPass = accPass

#     def __showPass(self):
#         print(f"Password = {self.__accPass}")

#     def checkPass(self):
#         self.__showPass()

# a1 = Account(143801000115559, "Shivam123")
# # print(a1.__accPass)
# # a1.__showPass()
# a1.checkPass()



# # # #Abstraction Change PassWord Practice Question # # #

class Account:

    def __init__(self, accNum, accPass):
        self.accNum = accNum
        self.__accPass = accPass

    def __showPass(self):
        return self.__accPass

    def checkPass(self):
        print(self.__showPass())

    def changePassword(self):
        oldPass = input("Enter your old Password: ")

        if(oldPass == self.__showPass()):
            while(True):
                newPass = input("Enter New Password: ")
                confirmPass = input("Confirm Password: ")

                if(newPass == confirmPass):
                    self.__accPass = newPass
                    print("Password changed successfully!")
                    break

                else:
                    print("Password does not match!")
        else:
            print("Wrong Password, Try Again !")
            self.changePassword()



a1 = Account(14380100115559, "Shivam123")
# print(a1.showPass())
a1.checkPass()
a1.changePassword()
a1.checkPass()