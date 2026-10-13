def merge_sorted_lists(list1, list2):
    return sorted(list(set(list1) | set(list2)))


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

print(merge_sorted_lists(list1, list2))

