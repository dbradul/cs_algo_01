import array


def swap(arr, frm, to):
    arr[frm], arr[to] = arr[to], arr[frm]


def partition(arr, l, r):
    pivot_idx = median(arr, l, (l+r)/2, r)#r
    swap(arr, l, pivot_idx)
    pivot = arr[l]
    i = l+1

    for j in range(l+1, r+1):
        if arr[j]<pivot:
            swap(arr, j, i)
            i += 1

    swap(arr, l, i-1)
    return i-1


def median(arr, l, m, r):
    if arr[l] <= arr[m] <= arr[r]: return m
    if arr[l] <= arr[r] <= arr[m]: return r
    if arr[m] <= arr[l] <= arr[r]: return l
    if arr[m] <= arr[r] <= arr[l]: return r
    if arr[r] <= arr[l] <= arr[m]: return l
    if arr[r] <= arr[m] <= arr[l]: return m


def quick_sort_internal(arr, l, r):
    total_cmp_number = 0
    if l<r:
        partition_boundary = partition(arr, l, r)
        total_cmp_number += quick_sort_internal(arr, l, partition_boundary-1)
        total_cmp_number += quick_sort_internal(arr, partition_boundary+1, r)
        total_cmp_number += (partition_boundary-1 - l)
        total_cmp_number += (r - partition_boundary)
    return total_cmp_number


def quick_sort(arr):
    total_cmp_number = quick_sort_internal(arr, 0, len(arr)-1)
    return arr, total_cmp_number


if __name__ == '__main__':
    f = open("/home/db/Work/Projects/Stanford_CS_Algo/week_02/QuickSort.txt")
    arr = array.array("i", [int(num) for num in f.read().split()])
    #arr = array.array("i", [1,2,3,4,5,6,7,8,9,10])

    arr, total_cmp_number = quick_sort(arr)

    assert(all(arr[i]<arr[i+1] for i in xrange(len(arr)-1)))

    print total_cmp_number

