a = ['a', 'b', 'c', 'd', 'e']
b = ['d', 'e', 'a', 'b', 'c']
rotate = -4

def right_rotate_list(lst, rotate):
    """
    O(n),
    """
    # The following line serves two porposes: (Assume list size n = 5)
    # 1) A rotation of right 7 (rotate = 7) is the same as the rotation of right 2 (i.e. rotation = rotation % n --> 7 % 5 = 2)
    # 2) A rotation of left 4 (rotate = -4) is the same as a right rotation of 2 (i.e. rotation = rotation % n --> -4 % 5 = 1)
    rotate %= len(lst) 
    for i in range(0, rotate):
        for j in range(i + rotate, len(lst) + i + 1, rotate):
            lst[i], lst[j % len(lst)] = lst[j % len(lst)], lst[i]

right_rotate_list(a, rotate)
print(a)
