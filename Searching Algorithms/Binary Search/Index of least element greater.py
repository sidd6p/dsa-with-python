lst = [-1, 0, 1, 1, 2, 5, 100, 282, 1111]


def index_of_least_element_greater(lst, element):
    low, high = 0, len(lst)
    sol = -1

    while low <= high:
        mid = low + (high - low) // 2
        if element < lst[mid]:
            sol = mid
            high = mid - 1
        elif element > lst[mid]:
            low = mid + 1
        else:
            low = mid + 1

    return sol


print(f"{index_of_least_element_greater(lst, 1)}")
