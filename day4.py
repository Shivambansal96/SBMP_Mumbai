# # # # # Recursion # # # # # 

# def printElementsOfList(arr, i):

#     if(i == len(arr)):
#         return

#     print(arr[i])
#     printElementsOfList(arr, i+1)

# arr = [10, 20, 12, 31]
# printElementsOfList(arr, 0)



# # # ## backTracking # # # # 

def countTotalPaths(i, j , n, m):

    # Dead End
    if(i == n or j == m):
        return 0
    # Destination
    if(i == n - 1 & j == m - 1):
        return 1

    # Move Rightwards
    rightWards = countTotalPaths(i, j+1, n , m)
    # Move Downwards
    downWards = countTotalPaths(i+1, j, n , m)
    return rightWards + downWards


n = 3
m = 3
print(f" Total paths = {countTotalPaths(0, 0, n, m)}")
