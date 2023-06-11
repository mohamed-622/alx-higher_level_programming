#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_val = my_list[0]
        for num in my_list:
            if num > max_val:
                max_val = num
        return max_val
    else:
        return None
