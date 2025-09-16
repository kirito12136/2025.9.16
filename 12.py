def merge_sequential_lists(A, B):
    i = 0  # 指向A的指针
    j = 0  # 指向B的指针
    C = []  # 结果顺序表

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < len(A):
        C.append(A[i])
        i += 1

    while j < len(B):
        C.append(B[j])
        j += 1

    return C