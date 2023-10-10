unsorted_arr = [60, 20, 10, 30, 50, 40]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            now = j
            nxt = j+1
            if arr[now] > arr[nxt]:
                arr[now], arr[nxt] = arr[nxt], arr[now]


print("Before Sorting:", unsorted_arr)
bubble_sort(unsorted_arr)
print("After Sorting:", unsorted_arr)
