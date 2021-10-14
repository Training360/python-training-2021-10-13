from functions import sum_numbers, count_spaces, calculate_average


def test_sum_numbers():  # Függvény = teszteset
    result = sum_numbers(2, 3)  # Tesztelendő függvény meghívása
    assert result == 5


def test_sum_numbers_zero():  # Függvény = teszteset
    result = sum_numbers(0, 0)  # Tesztelendő függvény meghívása
    assert result == 0


def test_sum_numbers_mixed():  # Függvény = teszteset
    result = sum_numbers(5, -6)  # Tesztelendő függvény meghívása
    assert result == -1


def test_sum_numbers_negatives():  # Függvény = teszteset
    result = sum_numbers(-5, -6)  # Tesztelendő függvény meghívása
    assert result == -11

def test_count_spaces_two():
    assert count_spaces("aaa bbb ccc") == 2

def test_count_spaces_leading():
    assert count_spaces("    aaabbbccc") == 3

def test_count_spaces_zero():
    assert count_spaces("xyz") == 0

def test_calc_average():
    assert calculate_average([1, 2, 3]) == 2

def test_calc_average_empty():
    assert calculate_average([]) == 0