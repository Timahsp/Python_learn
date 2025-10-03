'''
❓ Question: Selection Sort

You are given an array of integers.
Your task is to sort the array in ascending order using the Selection Sort algorithm.

Constraints:

Do not use Python’s built-in sort() function.

Implement the sorting logic by repeatedly selecting the minimum element from the unsorted part of the array and swapping it with the first unsorted element.

Example 1:
Input:  [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]

Example 2:
Input:  [3, 1, 4, 2]
Output: [1, 2, 3, 4]

✨ Bonus Task:

Print the array after each swap so you can see how the array gradually gets sorted.

'''

class SelectionSort():
    def sorting(self, arr):
        arr_length = len(arr)
        for i in range(arr_length):
            min_idx = i
            for j in range(i+1, arr_length):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
        
        return arr


selectionSort = SelectionSort()
arr = [64, 25, 12, 22, 11]
output = selectionSort.sorting(arr)
print (output)
