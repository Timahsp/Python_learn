'''
❓ Question:

You are given an array of integers.
Your task is to count how many inversions are present in the array and then sort the array in ascending order.

👉 An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].

Example 1:
Input:  [3, 4, 6, 5, 2]  
Output:  
Inversions = 5  
Sorted array = [2, 3, 4, 5, 6]

Example 2:
Input:  [1, 2, 3]  
Output:  
Inversions = 0  
Sorted array = [1, 2, 3]

✨ Your Task:
Write a Python function that takes an array as input.
It should return:
    The number of inversions in the array.
    The sorted array.
'''

class Inversion:
    def array_sorting(self, arr):
        count = 0
        arrlen = len(arr)
        newarr = []
        for value in range(arrlen):
            for nextvalue in range(value+1,arrlen):
                if arr[value]>arr[nextvalue]:
                    count +=1
                    newarr.append((arr[value],arr[nextvalue]))
                    arr[value],  arr[nextvalue] = arr [nextvalue], arr[value]
        return count,newarr,arr

inversion = Inversion()
array1 = [1, 2, 1, 12 ,16 ,11]   
a,b,c = inversion.array_sorting(array1)
print("sorted array : ", c)
print("Inversion coun is ", a ,"and inversion pairs are ", b)