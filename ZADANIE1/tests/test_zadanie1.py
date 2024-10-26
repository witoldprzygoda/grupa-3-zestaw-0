from ZADANIE1.zadanie1 import permutacja

def test_permutacja_przyklad():
    # Przykład z treści zadania: x = 1, y = 1, z = 2, n = 3
    wynik = permutacja(1, 1, 2, 3)
    oczekiwany = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], 
                  [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
    assert wynik == oczekiwany

def test_permutacja_zero():
    # Przypadek z minimalnymi wartościami: x = 0, y = 0, z = 0, n = 0
    wynik = permutacja(0, 0, 0, 0)
    oczekiwany = []  # Brak współrzędnych, które nie sumują się do 0
    assert wynik == oczekiwany

def test_permutacja_brak_ograniczen():
    # Przypadek, gdzie żaden warunek nie ogranicza wyników: x = 1, y = 1, z = 1, n = 10
    wynik = permutacja(1, 1, 1, 10)
    oczekiwany = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], 
                  [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    assert wynik == oczekiwany

def test_permutacja_pelne_ograniczenie():
    # Przypadek, gdy x = 1, y = 1, z = 1, n = 1
    wynik = permutacja(1, 1, 1, 1)
    oczekiwany = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    assert wynik == oczekiwany

def test_permutacja_wieksze_zakresy():
    # Przypadek dla x = 2, y = 2, z = 2, n = 3
    wynik = permutacja(2, 2, 2, 3)
    oczekiwany = [
        [0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 2, 0], 
        [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 1], 
        [1, 2, 2], [2, 0, 0], [2, 0, 2], [2, 1, 1], [2, 1, 2], [2, 2, 0], 
        [2, 2, 1], [2, 2, 2]
    ]
    assert wynik == oczekiwany


def test_permutacja_duze_n_z_niskimi_xyz():
    # Przypadek z dużą wartością n, ale małymi zakresami x, y, z
    wynik = permutacja(2, 2, 2, 10)
    oczekiwany = [
        [0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2],
        [0, 2, 0], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2],
        [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2],
        [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2],
        [2, 2, 0], [2, 2, 1], [2, 2, 2]
    ]
    assert wynik == oczekiwany
