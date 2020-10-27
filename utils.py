import numpy as np
import time

numbers = [i for i in range(1,11)]

def get_random_numbers():
    n = numbers[:]
    np.random.shuffle(n)
    return n

def get_sorted_numbers():
    return numbers

def swap(lyst,i,j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def print_result(func,*kwargs):
    start = time.time()
    result = func(*kwargs)
    print("Result:", result, "   COST TIME:", time.time() - start)