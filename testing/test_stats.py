from stats import sort_list, find_median

def test_sort_list():
    list = [5, 0, 9, 1, 2, 3]
    assert sort_list(list) == [0, 1, 2, 3, 5, 9]

def test_find_median():
    list = [5, 0, 9, 1, 2, 3]
    assert find_median(list) == 2.5