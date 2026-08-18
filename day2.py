# # # # # # # # # # name1 = input("Enter First Name = ") # Shivam
# # # # # # # # # # name2 = input("Enter Second Name = ") #Mohini
# # # # # # # # # # name3 = name1 + name2

# # # # # # # # # # a = name3.count("a") 
# # # # # # # # # # b = name3.count("e")
# # # # # # # # # # c = name3.count("i") 
# # # # # # # # # # d = name3.count("o") 
# # # # # # # # # # e = name3.count("u") 

# # # # # # # # # # count = a + b+ c + d + e
# # # # # # # # # # print(count)



# # # # # # # # # arr = [100, 20, 30, 40, 50]

# # # # # # # # # # a = arr.count(10)
# # # # # # # # # # b = arr.sort(reverse=True) # Returns nothing // Changes are made in main list.

# # # # # # # # # # print(a)
# # # # # # # # # # print(b)
# # # # # # # # # # print(arr)

# # # # # # # # # c = arr.reverse()
# # # # # # # # # print(arr)


# # # # # # # # # mov1 = input("Enter your fav movie 1: ")
# # # # # # # # # mov2 = input("Enter your fav movie 2: ")
# # # # # # # # # mov3 = input("Enter your fav movie 3: ")

# # # # # # # # # movieList = []

# # # # # # # # # movieList.append(mov1)
# # # # # # # # # movieList.append(mov2)
# # # # # # # # # movieList.append(mov3)
# # # # # # # # # print(movieList)

# # # # # # # # moviesList = list(map(str, input().split()))
# # # # # # # # print(moviesList)



# # # # # # # # arr = [("Shivam", 98), ("Alex", 100)]


# # # # # # # a = [1, 2]
# # # # # # # b = [3, 4]
# # # # # # # print(a + b)

# # # # # # # # print(type(a))


# # # # # # name = input("Enter your name: ")
# # # # # # age = input("Enter your age: ")
# # # # # # branch = input("Enter your branch: ")

# # # # # # tup = (name, age, branch)

# # # # # # print(f"Name: {tup[0]}, Age: {tup[1]}, Branch: {tup[2]}")




# # # # # # num = int(input("Enter a num: "))

# # # # # # for i in range(1, 11):
# # # # # #     print(f"{num} x {i} = {num * i}")



# # # # # i = 0
# # # # # while(i <= 5):

# # # # #     i += 1
# # # # #     if(i == 3):
# # # # #         break
        
# # # # #     print(i)


# # # # arr = [1, 2, 3]
# # # # # print(arr)

# # # # for i in arr: 
# # # #     print(arr[i], end=" ")


# # # # n = int(input("Enter a num: "))
# # # arr = []
# # # n = 10
# # # for i in range(1, n+1):
# # #     sq = i *i
# # #     arr.append(sq)
# # #     # arr.append(i*i)
# # #     # arr.append(i**2)

# # # # print(arr)

# # # target = int(input("Enter the number you want to search: "))

# # # if(target in arr):
# # #     print(f"Target Found at index {arr.index(target)}")
# # # else:
# # #     print("Target NOT Found")



# # # n = int(input("Enter a num: "))

# # # total = 0

# # # for i in range(n+1):
# # #     total += i

# # # print(f"Sum = {total}")


# # n = int(input("Enter n: "))
# # r = int(input("Enter r: "))

# # fact = 1
# # for i in range(1, n+1):
# #     fact *= i

# # num = fact
# # fact = 1
# # denom = n - r

# # for i in range(1, denom+1):
# #     fact *= i

# # denom = fact
# # perm = num / denom


# # print(f"Permutation = {perm}")



# myDict = {
#     'name': "Shivam",
#     'marks': {
#         'python': 99,
#         'webDev': 342,
#         'Java': 2
#     }
# }

# myDict.update({'isTrainer': True})

# # print(myDict['marks']['web Dev'])
# # print(myDict.values())
# # print()

# # for i in myDict.values():
# #     print(i)

# # print("DEMO CHECK")
# # print(myDict['names'])
# # print(myDict.get('names'))


# # print(myDict.items())
# # print()

# # for i in myDict.items():
# #     print(i[1])


# # myDict = {}

# # sub1 = input(f"Enter subject1 name: ")
# # m1 = int(input(f"Enter marks of {sub1}: "))

# # sub2 = input(f"Enter subject2 name: ")
# # m2 = int(input(f"Enter marks of {sub2}: "))

# # sub3 = input(f"Enter subject3 name: ")
# # m3 = int(input(f"Enter marks of {sub3}: "))

# # myDict.update({sub1: m1})
# # myDict.update({sub2: m2})
# # myDict.update({sub3: m3})

# # print(myDict)



# myDict = {}

# for i in range(3):
#     sub = input(f"Enter subject{i+1} name: ")
#     marks = int(input(f"Enter marks of {sub}: "))
    
#     print()

#     myDict.update({sub: marks})

# print(myDict)


arr = [1, 1, 2, 1, 3, 4, 1, 3, 4]
freqCalc = {}

for i in range(len(arr)):

    if(arr[i] in freqCalc):
        freqCalc.update({arr[i]: freqCalc[arr[i]] + 1})

    else:
        freqCalc.update({arr[i]: 1})

print(freqCalc)