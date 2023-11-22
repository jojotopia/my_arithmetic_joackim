def pgcd(a, b):
    """Calcul le plus grand commun diviseur de deux nombres entiers.

    Args:
        a (int): le premier nombre entier.
        b (int): le deuxième nombre entier.

    Returns:
        int: le PGCD de a et b.
    """
    # Appliquer l'algorithme d'Euclide
    while b != 0:
        a, b = b, a % b
    return a