# with linear search
arr = [1, 2, 2, 2, 3, 4, 5]
ele_check = 2

def first_occurence(arr, ele_check):
    my_list = []
    n = len(arr)
    for i in range(n):
        if (arr[i] == ele_check):
            my_list.append(i)
            
    print("First occurence of", ele_check, "is at index", min(my_list) )
    print("Last occurence of" , ele_check, "is at index", max(my_list) )


first_occurence(arr, 2)
