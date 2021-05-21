def smallest(array, k):
    array_sort = sorted(array)
    return array_sort[:k]


if __name__ == "__main__":
   array = [10,4,5,2,12,6]
   print(smallest(array, 2))
