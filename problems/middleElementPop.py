my_stack = [21, 32, 45, 63, 78]  # original stack1
print("Main Stack",my_stack)

def middle_ele_remove(main_stack):
    s1 = []  # empty stack
    middle_ele_index = len(main_stack)//2

    for i in range(middle_ele_index): 
        s1.append(main_stack.pop(0)) 

    main_stack.pop(0) #pop middle element

    for i in range(len(s1)):
        main_stack.insert(i, s1.pop(0))

    print("Result",main_stack) #printing result


middle_ele_remove(my_stack)
