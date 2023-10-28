def cbis(a_list):
    POP = 0
    for i in range(1, len(a_list)):
        COP = i
        key = a_list[COP]
        if key >= a_list[POP]:
            place = binary_loc_finder(a_list, POP + 1, COP - 1, key)
        else:
            place = binary_loc_finder(a_list, 0, POP - 1, key)
        POP = place
        a_list = place_inserter(a_list, place, COP)
    return a_list

def binary_loc_finder(a_list, start, end, key):
    if start == end:
        if a_list[start] > key:
            return start
        else:
            return start + 1
    if start > end:
        return start
    else:
        mid = (start + end) // 2
        if a_list[mid] < key:
            return binary_loc_finder(a_list, mid + 1, end, key)
        elif a_list[mid] > key:
            return binary_loc_finder(a_list, start, mid - 1, key)
        else:
            return mid
        
def place_inserter(a_list, start, end):
    temp = a_list[end]
    for k in range(end, start - 1, -1):
        a_list[k] = a_list[k - 1]
    a_list[start] = temp
    return a_list