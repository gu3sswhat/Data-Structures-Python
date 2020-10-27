from utils import get_sorted_numbers,print_result
import time
"""
二叉搜索可能比顺序搜索要更为高效，
但二叉搜索有一个额外的整体性代价，就是必须保持列表是有序的
"""
numbers = get_sorted_numbers()
print("The Sequence is ",numbers)

def binarySearch(target,sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
        time.sleep(0.1)
    return -1

if __name__ == '__main__':
    target = 9
    print_result(binarySearch,target,numbers)