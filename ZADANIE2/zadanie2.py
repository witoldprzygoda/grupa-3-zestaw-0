def odwracanie_iteracyjnie(L, left, right):
    """Odwraca elementy listy L od indeksu left do right (wersja iteracyjna)."""
    # Obsługa ujemnych indeksów
    # Jeśli left i right są poza zakresem lub left > right, nie zmieniamy listy

    return L

def odwracanie_rekurencyjnie(L, left, right):
    """Odwraca elementy listy L od indeksu left do right (wersja rekurencyjna)."""
    # Obsługa ujemnych indeksów
    # Jeśli left i right są poza zakresem lub left > right, nie zmieniamy listy

    return L


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6]
    print("Oryginalna lista:", lista)

    # wersja iteracyjna
    print("Iteracyjne odwracanie od 1 do 4:", odwracanie_iteracyjnie(lista[:], 1, 4))

    # wersja rekurencyjna
    print("Rekurencyjne odwracanie od 1 do 4:", odwracanie_rekurencyjnie(lista[:], 1, 4))
