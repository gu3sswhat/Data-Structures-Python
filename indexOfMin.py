from utils import get_random_numbers, print_result
import time

numbers = get_random_numbers()
print("The Sequence is ",numbers)

def indexOfMin(lyst):
    """Returns the index of the minimun item"""
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
        time.sleep(0.1)
    return minIndex
if __name__ == '__main__':
    print_result(indexOfMin,numbers)