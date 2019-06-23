def right_rotate_list(lst, rotate):
    """
    O(n) in place solution
    """
    # The following line serves two purposes: (Assume list size n = 5)
    # 1) A rotation of right 7 (rotate = 7) is the same as the rotation of right 2 (i.e. rotation = rotation % n --> 7 % 5 = 2)
    # 2) A rotation of left 4 (rotate = -4) is the same as a right rotation of 1 (i.e. rotation = rotation % n --> -4 % 5 = 1)
    rotate %= len(lst) 
    for i in range(0, rotate):
        for j in range(i + rotate, len(lst) + i + 1, rotate):
            lst[i], lst[j % len(lst)] = lst[j % len(lst)], lst[i]

a = [chr(ord('a') + x) for x in range(26)] # full alphabet
rotate = -4
right_rotate_list(a, rotate)
print(a)

# Still contains a bug
