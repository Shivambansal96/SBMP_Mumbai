# # # # # # # # # FORM VALIDATOR 

# # # # # # name = input("Enter your Name: ").strip()
# # # # # # email = input("Enter your Email: ")
# # # # # # password = input("Enter your Password: ")
# # # # # # flag = True

# # # # # # if(' ' not in name):
# # # # # #     flag=False
# # # # # #     print("Invalid Full Name")

# # # # # # if('@' not in email or not(email.endswith(".com"))):
# # # # # #     flag=False
# # # # # #     print("Invalid Email Address")

# # # # # # if(len(password) < 6 or ' ' in password):
# # # # # #     flag=False
# # # # # #     print("Invalid Password")

# # # # # # if(flag):
# # # # # #     print("Form Submitted Successfully.")




# # # # # newSet = {8, 2,2, 3, 1, 4}
# # # # # # print(type(newSet))
# # # # # # print(newSet)

# # # # # # newSet.add(10)
# # # # # newSet.pop()

# # # # # print(newSet)


# # # # # n = int(input("Enter the number of Students: "))
# # # # # studentList = []
# # # # # for i in range(n):
# # # # #     name = input("Enter your name: ")
# # # # #     marks = int(input("Enter your marks: "))

# # # # #     tup = (name, marks)

# # # # #     studentList.append(tup)

# # # # # print(studentList)

# # # # studentList = [("Shivam", 98), ("Mohini", 100), ("S"
# # # # "hivam", 90)]

# # # # names = set()
# # # # for i in studentList:
# # # #     names.add(i[0])

# # # # for i in names:
# # # #     totalSum = 0
# # # #     count = 0

# # # #     for name, mark in studentList:
# # # #         if(name == i):
# # # #             totalSum += mark
# # # #             count += 1

# # # #     print(f"Average of {i} = {totalSum / count}")


# # # # # ## # FUNCTIONS #####




# # # # def listLen(arr):
# # # #     print(len(arr))

# # # # arr = [24, 64, 23, 76]
# # # # listLen(arr)


# # # # def listLen(arr):
# # # #     for i in arr:
# # # #         print(i, end=" ")

# # # # arr = [24, 64, 23, 76]
# # # # listLen(arr)


# # # # def factorial(n):
# # # #     fact = 1
# # # #     for i in range(1, n+1):
# # # #         fact *= i

# # # #     return fact

# # # # n = 5
# # # # print(f"Factorial of {n} = {factorial(n)}")



# # # # def usdConversionToINR(dollars):
# # # #     return dollars * 90

# # # # dollars = float(input("Enter the number of dollars: "))

# # # # print(f"${dollars} = Rs {usdConversionToINR(dollars)}")


# # # a = 9987656/3

# # # # print(round(a, 2))
# # # print(f"{a:.2f}")

# # def factorial(n):
# #     fact = 1
# #     for i in range(1, n+1):
# #         fact *= i

# #     return fact


# # def pORc():
# #     n = int(input("Enter value of n: "))
# #     r = int(input("Enter value of r: "))
# #     userInput = int(input("What do you want to perform: \n1. Permutation\n2. Combination = "))

# #     num = factorial(n)
# #     denom = factorial(n - r)

# #     if(userInput == 1):
# #         perm = num / denom
# #         print(f"Permutation = {perm}")

# #     elif(userInput == 2):
# #         comb = num / denom * factorial(r)
# #         print(f"Combination = {comb}")

# #     else:
# #         print("Invalid Input")


# # pORc()



# # ## # ## Recursion # # # ## 


# # def printNTo1(n):

# #     if(n == 1):
# #         return 
# #     print(n)
# #     printNTo1(n-1)

# # printNTo1(3)



# def learningCallStack(n):
#     if(n == 0):
#         return 

#     print(f"INSIDE Function, BEFORE n = {n}")
#     learningCallStack(n - 1)
#     print(f"INSIDE Function, AFTER n = {n}")

# print("Code Starts")
# learningCallStack(3)
# print("Learnt Recursion through Call Stack !!!")


def print1ToN(i, n):

    if(i == n+1):
        return

    print(i)
    print1ToN(i+1, n)

print1ToN(1, 5)