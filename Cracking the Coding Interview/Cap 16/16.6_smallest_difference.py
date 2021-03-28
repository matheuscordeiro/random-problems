def smallest_difference(A, B):
    A = sorted(A)
    B = sorted(B)
    pos_A = pos_B = 0
    smallest = abs(B[0] - A[0])
    while pos_A < len(A) and pos_B < len(B):
        if A[pos_A] > B[pos_B]:
            smallest = min(smallest, A[pos_A] - B[pos_B])
            pos_B += 1
        elif B[pos_B] > A[pos_A]:
            smallest = min(smallest, B[pos_B] - A[pos_A])
            pos_A += 1
        else:
            pos_A += 1
            pos_B += 1

    return smallest


if __name__ == "__main__":
    A = [1,3,15,11,2]
    B = [23,127,235,19,8]
    print(smallest_difference(A, B))