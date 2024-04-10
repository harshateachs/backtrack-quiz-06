from typing import List


def list_operations(list1, list2, operations):
    merged_list = list1 + list2
    for operation in operations:
        if operation == "M":
            pass
        elif operation == "R":
            merged_list = list(set(merged_list))
        elif operation == "S":
            merged_list.sort()
        else:
            merged_list.sort(reverse=True)

    return merged_list


# Sample test cases
if __name__ == "__main__":
    # Test cases
    assert list_operations([1, 3, 2], [4, 3, 5], 'MRS') == [1, 2, 3, 4, 5]
    assert list_operations([7, 5, 3], [4, 2, 1], 'RMV') == [7, 5, 4, 3, 2, 1]
    assert list_operations([4, 1, 6], [2, 5, 3], 'MS') == [1, 2, 3, 4, 5, 6]
    assert list_operations([10, 20, 30], [30, 40, 50], 'MRV') == [50, 40, 30, 20, 10]
    assert list_operations([3, 2, 1], [4, 5, 4], 'RSM') == [1, 2, 3, 4, 5]

    print("All test cases passed!")
