unsorted_arr = [60, 20, 10, 30, 50, 40]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest_ele = i
        for j in range(i+1, n):
            if arr[j] < arr[smallest_ele]:
                smallest_ele = j
        arr[i], arr[smallest_ele] = arr[smallest_ele], arr[i]


print("Before Sorting:", unsorted_arr)
selection_sort(unsorted_arr)
print("After Sorting:", unsorted_arr)
