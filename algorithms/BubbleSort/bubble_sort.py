import time
from util import time_it

@time_it
def bubble_sort(elements):
    """ sort the elements in a list using bubble sort alogorithm"""
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        
        if not swapped:
            break

@time_it
def bubble_sort_based_on_key(elements, key):
    """ Bubble sort based on a key of element in the list"""
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        
        if not swapped:
            break

if __name__ == '__main__':
    #elements = [5, 9, 2, 1, 67, 34, 88, 34, 56, 23, 43, 4, 8, 3, 31, 29, 40, 51, 22, 35]
    elements = ["mani", "dhoni", "amir", "dhruv", "rana"]
    print("elements to be sorted ====> %s"%(elements))
    print("\n")
    bubble_sort(elements)
    print("elements after sorted using bubblesort ====> %s"%(elements))
    print("\n")


    elements = [
        { 'name': 'amir', 'trans_amt': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'trans_amt': 400, 'device': 'google-pixel'},
        { 'name': 'karthi', 'trans_amt': 200, 'device': 'vivo'},
        { 'name': 'mona', 'trans_amt': 800, 'device': 'iphon-8'},
        { 'name': 'rana', 'trans_amt': 1100, 'device': 'redmi'}
    ]
    bubble_sort_based_on_key(elements, 'device')
    print("elements after sorted using bubblesort based on key ====> %s"%(elements))
