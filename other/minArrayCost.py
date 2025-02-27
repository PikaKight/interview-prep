"""Given an array of n positive integers, its cost is
the Sum of (arr[i] - arr [i-1])^2 from i=1 to i len(arr) - 1

Insert any integer at any location of the array such that the
cost of the array is minimized. Find the minimum possible cost
the array after inserting exactly one element.

Example
a = [1, 3, 5, 2, 10]

The cost of the array before 
insertion = (1 - 3)^2 + (3-5)^2 + (5-2)^2 + (2- 10)^2 = 81.

Two of many scenarios are shown below.

1. Insert 4 between 3 and 5, cost of 
array = (1 - 3)^2+(3-4)^2+ (4-5)^2 +(5-2)^2+ (2 - 10)^2 = 79.

2. Insert 6 between 2 and 10, cost of 
array =(1 - 3)^2 + (3 - 5)^2 +(5- 2)^2+ (2 - 6)^2 + (6- 10)^2 = 49.

It can be proven that 49 is the minimum cost possible. Return 49.

Function Description
Complete the function getMinimumCost in the editor below.

getMinimumCost has the following parameter:
int arr[n]: an array of integers

Returns
long_int: the minimum possible cost of the array after inserting one element

Constrains
2 <= n <= 10^4
1 <= arr[i] <= 10^5
"""

def getMinimumCost(arr: list) -> int:

    index = 0
    minCost = 0
    maxDiff = 0

    n = len(arr)

    for i in range(0, n-1):
        diff = abs(arr[i] - arr[i+1])

        if maxDiff < diff:
            maxDiff = diff
            index = i

    idealInt = (abs(arr[index] - arr[index + 1])) // 2 + min(arr[index], arr[index + 1])

    arr.insert(idealInt, index+1)

    for i in range(0, n-1):
        minCost += pow(arr[i] - arr[i+1], 2)

    return (minCost, idealInt, index)

if __name__ == "__main__":
    
    arr = [1, 3, 99, 100, 10, 15, 2]

    print(getMinimumCost(arr))
