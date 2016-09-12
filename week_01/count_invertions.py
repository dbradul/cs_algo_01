from random import randint


def sort_and_count_inversions(A):
    if len(A) == 1:
        return A, 0
    else:
        B, n1 = sort_and_count_inversions(A[:len(A) / 2])
        C, n2 = sort_and_count_inversions(A[len(A) / 2:])
        D, n3 = merge_and_count_inversions(B, C)
        return D, (n1 + n2 + n3)


def merge_and_count_inversions(B, C):
    i, j, k = 0, 0, 0
    num_inversions = 0
    D = [0] * (len(B) + len(C))

    while (i < len(B) and j < len(C)):
        if B[i] <= C[j]:
            D[k] = B[i]
            # D.append(B[i])
            i += 1
        else:
            D[k] = C[j]
            # D.append(C[j])
            j += 1
            num_inversions += (len(B) - i)
        k += 1

	# D.extend(B[i:])
	# D.extend(C[j:])
    if i < len(B):
        D[k:] = B[i:]
    elif j < len(C):
        D[k:] = C[j:]

    return D, num_inversions


def brute_force(A):
    inversions = 0
    for i in xrange(0, len(A)):
        for j in xrange(i + 1, len(A)):
            if A[i] > A[j]:
                inversions += 1
    return inversions


def my_assert(A):
    assert brute_force(A) == sort_and_count_inversions(A)[1]


def generate_array():
    arr = [0] * randint(1, 1000)
    for i in xrange(0, len(arr)):
        arr[i] = randint(0, 1000)
    return arr


if __name__ == '__main__':
    f = open("integerArray.txt")
    list = f.read().split()
    # print sort_and_count_inversions(list)[1]

    # tests
    for i in xrange(0, 100):
        A = generate_array()
        my_assert(A)

    my_assert([1])
    my_assert([1, 1])
    my_assert([1, 1, 1])
    my_assert([1, 1, 1, 1])
    my_assert([1, 1, 1, 1, 1])
    my_assert([1, 2, 3, 4, 5, 6])
    my_assert([2, 1])
    my_assert([2, 1, 1])
    my_assert([2, 1, 1, 1])
    my_assert([2, 1, 1, 1, 1])
    my_assert([2, 1, 1, 1, 0])
    my_assert([6, 5, 4, 3, 2, 1])

    my_assert([1, 3, 5, 2, 4, 6])
    my_assert([1, 3, 5, 2, 4, 6, 7])
    my_assert([1, 5, 3, 2, 4, 6])
    my_assert([1, 5, 3, 2, 4, 6, 7])

    my_assert([2, 1, 1, 1, 1, 0])
    my_assert([2, 1, 1, 1, 1, 3])
    my_assert([4, 1, 1, 1, 1, 3])
    my_assert([4, 1, 1, 1, 1, 3, 5])
    my_assert([4, 1, 1, 1, 1, 3, 5, 5])

    my_assert([1, 2, 3, 3, 2, 1])
    my_assert([1, 2, 3, 1, 2, 3])
    my_assert([1, 2, 3, 0, 0, 0])
