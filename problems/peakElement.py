arr = [60, 20, 90, 110, 10]
start = 0
end = len(arr)-1


def peak_check(arr, start, end):  # arr = [60, 20, 90, 110, 10]
    mid = (start + end)//2
    prev = mid-1
    nxt = mid+1

    if (arr[prev] < arr[mid] > arr[nxt]):
        print("Peak Element", arr[mid])
        exit
    elif (arr[mid] < arr[nxt]):
        start = mid
        peak_check(arr, start, end)
    elif (arr[mid] < arr[prev]):
        end = mid
        peak_check(arr, start, end)


peak_check(arr, start, end)
