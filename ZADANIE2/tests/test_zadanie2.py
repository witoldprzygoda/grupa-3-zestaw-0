from ZADANIE2.zadanie2 import odwracanie_iteracyjnie, odwracanie_rekurencyjnie  

# Test przypadków podstawowych
def test_odwracanie_pustej_listy():
    assert odwracanie_iteracyjnie([], 0, 0) == []
    assert odwracanie_rekurencyjnie([], 0, 0) == []

def test_odwracanie_jednoelementowej_listy():
    assert odwracanie_iteracyjnie([1], 0, 0) == [1]
    assert odwracanie_rekurencyjnie([1], 0, 0) == [1]

# Test pełnego odwrócenia listy
def test_odwracanie_pelna_lista():
    assert odwracanie_iteracyjnie([1, 2, 3, 4], 0, 3) == [4, 3, 2, 1]
    assert odwracanie_rekurencyjnie([1, 2, 3, 4], 0, 3) == [4, 3, 2, 1]

# Test częściowego odwrócenia listy
def test_odwracanie_fragmentu_listy():
    assert odwracanie_iteracyjnie([1, 2, 3, 4, 5, 6], 1, 4) == [1, 5, 4, 3, 2, 6]
    assert odwracanie_rekurencyjnie([1, 2, 3, 4, 5, 6], 1, 4) == [1, 5, 4, 3, 2, 6]

# Test odwracania elementów na początku listy
def test_odwracanie_poczatkowych_elementow():
    assert odwracanie_iteracyjnie([10, 20, 30, 40, 50], 0, 2) == [30, 20, 10, 40, 50]
    assert odwracanie_rekurencyjnie([10, 20, 30, 40, 50], 0, 2) == [30, 20, 10, 40, 50]

# Test odwracania elementów na końcu listy
def test_odwracanie_koncowych_elementow():
    assert odwracanie_iteracyjnie([1, 2, 3, 4, 5], 2, 4) == [1, 2, 5, 4, 3]
    assert odwracanie_rekurencyjnie([1, 2, 3, 4, 5], 2, 4) == [1, 2, 5, 4, 3]

# Test przypadków granicznych (left > right lub indeksy poza zakresem)
def test_odwracanie_graniczne():
    assert odwracanie_iteracyjnie([1, 2, 3], 2, 1) == [1, 2, 3]  # left > right, brak zmian
    assert odwracanie_rekurencyjnie([1, 2, 3], 2, 1) == [1, 2, 3]

    # left i right poza zakresem, oczekiwany brak zmian
    assert odwracanie_iteracyjnie([1, 2, 3], -1, 5) == [1, 2, 3]
    assert odwracanie_rekurencyjnie([1, 2, 3], -1, 5) == [1, 2, 3]

def test_odwracanie_ujemne_indeksy():
    # Ujemne indeksy wewnątrz zakresu listy
    assert odwracanie_iteracyjnie([1, 2, 3, 4, 5], -4, -2) == [1, 4, 3, 2, 5]
    assert odwracanie_rekurencyjnie([1, 2, 3, 4, 5], -4, -2) == [1, 4, 3, 2, 5]

    # Kombinacja dodatnich i ujemnych indeksów
    assert odwracanie_iteracyjnie([10, 20, 30, 40, 50, 60], 1, -2) == [10, 50, 40, 30, 20, 60]
    assert odwracanie_rekurencyjnie([10, 20, 30, 40, 50, 60], 1, -2) == [10, 50, 40, 30, 20, 60]
