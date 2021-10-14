from functions import sum_numbers


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
