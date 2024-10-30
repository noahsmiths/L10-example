from typing import List


def sort_list(list: List[int]) -> List[int]:
    for i in range(len(list)):
        for j in range(i, len(list) - 1):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    
    return list

def find_median(list: List[int]):
    sorted_test = sort_list(list)

    return sorted_test[len(sorted_test) // 2]