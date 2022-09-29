#!/usr/bin/python3
"""Defines a function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers rep the Pascal’s triangle"""

    list_of_lists = []
    list_counter = 4
    # list_counter is 4 because the list we want to always begin operation on
    # is index[2] of list_of_lists ie [1, 2, 1]
    # due to this, the formula on line 39 (value formula) works

    # checking if n is greater than or equal to zero
    if n <= 0:
        return list_of_lists
    elif n == 1:
        list_of_lists = [[1]]
        return list_of_lists
    elif n == 2:
        list_of_lists = [[1], [1, 1]]
        return list_of_lists
    elif n == 3:
        list_of_lists = [[1], [1, 1], [1, 2, 1]]
        return list_of_lists
    elif n > 3:
        list_of_lists = [[1], [1, 1], [1, 2, 1]]

        # looping to append onto the list_of_lists list
        for iteration in range(3, n):
            nth_list = [1]
            counter = 0
            idx = 1
            value = 0

            # looping to create the individual indexes(lists)
            # of list_of_lists
            while counter < list_counter - 3:
                value = list_of_lists[list_counter - 2][idx - 1] \
                        + list_of_lists[list_counter - 2][idx]
                nth_list.append(value)
                counter += 1
                idx += 1

            # appending the second last value,
            # which is equal to the second value of the list
            # then adding the last element, which is always 1
            nth_list.append(nth_list[1])
            nth_list.append(1)

            # appending the new list into the list_of_lists list
            list_of_lists.append(nth_list)
            list_counter += 1

        return list_of_lists
