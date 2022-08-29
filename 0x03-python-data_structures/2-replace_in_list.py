#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        for index, old_element in enumerate(my_list):
            if index != idx:
                continue
            elif index == idx:
                my_list[index] = element
        return my_list
