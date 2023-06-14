#!/usr/bin/python3


# replaces all occurences of an element by another.
def search_replace(my_list, old, new):
    new_list = []
    for i in my_list:
        if i == old:
            new_list.append(new)
        else:
            new_list.append(i)
    return new_list
