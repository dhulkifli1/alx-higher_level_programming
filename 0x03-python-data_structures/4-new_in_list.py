#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        new_list = my_list
        return new_list
    elif idx > len(my_list):
        new_list = my_list
        return new_list
    else:
        for index, old_element in enumerate(my_list):
            if index != idx:
                new_list.append(old_element)
            else:
                new_list.append(element)
        return new_list
