search_array = [10, 20, 30, 40, 50, 60]
key = 20

def binary_search(search_array, key, start, end):
    mid = (start+end)//2
    if key == search_array[mid]:
        print("Element found at position", mid+1)
        exit
    elif key < search_array[mid]:
        binary_search(search_array, key, start, mid-1)
    elif key > search_array[mid]:
        binary_search(search_array, key, mid+1, end)
    else:
        print("Element not found")


binary_search(search_array, key, 0, len(search_array)-1)
