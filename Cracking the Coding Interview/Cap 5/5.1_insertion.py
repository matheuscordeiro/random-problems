def insertion(M, N, i, j):
    all_ones = ~0
    left_ones = all_ones << (j + 1)
    right_ones = all_ones >> (i + 1)
    mask = left_ones | right_ones
    n_cleaned = N & mask
    m_shifted = M << i
    return '{0:b}'.format(n_cleaned | m_shifted)


if __name__ == "__main__":
    print(insertion(19,1024, 2,6)) 