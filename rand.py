import random


def random_array(arr):
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = random.randint(1, 20)
        arr[i] = int(shuffled_num.stdout)
    return arr
