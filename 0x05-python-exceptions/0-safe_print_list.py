#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        count = 0
        for index in range(x):
            try:
                print(my_list[index], end='')
                count += 1
            except IndexError:
                break
    except Exception:
        pass
    print()
    return count
