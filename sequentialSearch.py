from utils import get_random_numbers,print_result
import time

numbers = get_random_numbers()
print("The Sequence is ",numbers)

def sequentialSearch(target, lyst):
    """Returns the position of the target item found, or -1 otherwise"""
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
        time.sleep(0.1)
    return -1

if __name__ == '__main__':
    target = 8
    print_result(sequentialSearch,target,numbers)