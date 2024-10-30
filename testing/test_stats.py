from stats import sort_list_ascending, find_median

def test_sort_list_ascending():
    list = [5, 0, 9, 1, 2, 3]
    sorted_list = sort_list_ascending(list)

    assert sorted_list == [0, 1, 2, 3, 5, 9]

def test_find_median_even_amount():
    list = [5, 0, 9, 1, 2, 3]
    median = find_median(list)

    assert median == 2.5

def test_find_median_odd_amount():
    list = [5, 0, 9, 1, 2]
    median = find_median(list)

    assert median == 2