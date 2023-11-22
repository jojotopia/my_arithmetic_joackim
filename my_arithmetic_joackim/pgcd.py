def pgcd(a, b):
    """
    Calcule le plus grand commun diviseur (PGCD) de deux nombres entiers.

    Parameters
    ----------
    a : int
        Le premier nombre entier.
    b : int
        Le deuxième nombre entier.

    Returns
    -------
    int
        Le PGCD de a et b.

    Examples
    --------
    >>> pgcd(12, 18)
    6
    >>> pgcd(7, 13)
    1
    """
    if(b == 0):
        return a
    else:
        return pgcd(b, a % b)