# # # # # # # Recursion # # # # # 

# # # def printElementsOfList(arr, i):

# # #     if(i == len(arr)):
# # #         return

# # #     print(arr[i])
# # #     printElementsOfList(arr, i+1)

# # # arr = [10, 20, 12, 31]
# # # printElementsOfList(arr, 0)



# # # # # ## backTracking # # # # 

# # def countTotalPaths(i, j , n, m):

# #     # Dead End
# #     if(i == n or j == m):
# #         return 0
# #     # Destination
# #     if(i == n - 1 & j == m - 1):
# #         return 1

# #     # Move Rightwards
# #     rightWards = countTotalPaths(i, j+1, n , m)
# #     # Move Downwards
# #     downWards = countTotalPaths(i+1, j, n , m)
# #     return rightWards + downWards


# # n = 3
# # m = 3
# # print(f" Total paths = {countTotalPaths(0, 0, n, m)}")



# def spiralMatrix(mat, top, left, right, bottom):

#     if(top > bottom or left > right):
#         return

#     # TOP -> left to Right
#     for i in range(left, right+1):
#         print(mat[top][i], end=" ")

#     # RIGHT -> top to bottom
#     for i in range(top+1, bottom+1):
#         print(mat[i][right], end=" ")

#     # BOTTOM <- right to left
#     for i in range(right - 1, left-1, -1):
#         print(mat[bottom][i], end=" ")

#     # LEFT <- bottom to top
#     for i in range(bottom-1, top, -1):
#         print(mat[i][left], end=" ")


    
#     spiralMatrix(mat, top+1, left+1, right-1, bottom-1)
    

    

# mat = [
#     [1,  2,  3,  4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7],
# ]

# n = len(mat) - 1
# m = len(mat[0]) - 1

# spiralMatrix(mat, 0, 0, n, m)



# a = int(input("Enter a number:"))
    
# try:
#     a = int(input("Enter a number:"))
#     for i in range(1, 11):
#         print(a * i)

# except ValueError:
#     print("Input has to be a number")
#     # print(e)

# try:
#     a = int(input("Enter a number:"))
#     for i in range(1, 11):
#         print(a * i)

# except Exception as e:
#     print("Input has to be a number")
#     print(e)


# try:
#     a = int(input("Enter a number:"))
#     for i in range(1, 11):
#         print(a * i)

# except:
#     raise KeyError('Naaam nahi daalna h')



try:
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(a/b)

except ValueError:
    print("Input has to be a number")

except ZeroDivisionError:
    print("Number cannot be divisible by 0.")
