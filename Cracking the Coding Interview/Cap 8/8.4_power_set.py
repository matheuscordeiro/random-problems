import math
from itertools import combinations

def all_subsets2(array):
    print()
    for i in range(1, len(array)+1):
        subsets_size_i = combinations(array, i)
        for j in subsets_size_i:
            print(j)

def all_subsets1(array):
    counter = int(math.pow(2, len(array)))
    for i in range(counter):
        for j in range(len(array)):
            if (i & (1 << j)) > 0:
                print(array[j], end="")
        
        print("")


if __name__ == '__main__':
    array = [1,2,3]
    all_subsets2(array)