from util import time_it


@time_it
def linear_search(numbers_list, number_to_find):
    """find the index of number in the list using linear search"""
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index

    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    """find the index of number in the list using binary search"""

    left_index = 0
    right_index = len(numbers_list) - 1

    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

@time_it
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    """binary search using recursion"""
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index)//2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

@time_it
def find_all_occurances(numbers_list, number_to_find):
    """find index of all occurances of given number in the list"""
    index = binary_search(numbers_list, number_to_find)
    indexes = [index]

    #find the occurances in left side
    i = index - 1
    while i >= 0:
        if numbers_list[i] == number_to_find:
            indexes.append(i)
        else:
            break

        i -= 1
    
    #find the occurances in right side
    i = index + 1
    while i <= len(numbers_list) - 1:
        if numbers_list[i] == number_to_find:
            indexes.append(i)
        else:
            break

        i += 1
    
    return sorted(indexes)


if __name__ == '__main__':
    numbers_list = [i for i in range(1000001)]
    number_to_find = 1000000
    
    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index ===> {index} using linear search")
    print("\n")
    
    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index ===> {index} using binary search")
    print("\n")

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index ===> {index} using binary search recursive")
    print("\n")

    numbers_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    indexes = find_all_occurances(numbers_list, number_to_find)
    print(f"All Occurances of Number found at index ===> {indexes} using binary search")

