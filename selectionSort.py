from utils import get_random_numbers, print_result, swap
import time

"""
选择排序在各种情况下的复杂度为O(n^2)
"""

numbers = get_random_numbers()
print("The Sequence is ",numbers)

def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst,minIndex,i)
        i += 1
        time.sleep(0.1)
    return lyst

if __name__ == '__main__':
    print_result(selectionSort,numbers)