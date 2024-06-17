def sub(arr):
    return [arr[0] - i for i in arr[1:]] + sub(arr[1:]) if arr else []
    
    
def solution(arr1, arr2):
    return [(i ** 2 + j ** 2) ** 0.5 for i, j in zip(arr1, arr2)]
    
    
points1 = [4, 6, 5, 10, 11]
points2 = [2, 4, 1, 6, 8]

euclideanDistance = solution(sub(points1), sub(points2))
print(euclideanDistance)