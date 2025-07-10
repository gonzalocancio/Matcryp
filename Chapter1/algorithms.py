import pandas as pd
from IPython.display import display

def extended_gcd(a, b):
    if a == 0 and b == 0:
        raise ValueError("gcd is undefined for a = 0 and b = 0")
    
    u, g = 1, a
    x, y = 0, b
    if y == 0:
        return a, 1, 0
        
    while y != 0:
        q = g // y
        t = g % y
        s = u - q * x

        # Update variables for next iteration
        u, g = x, y
        x, y = s, t

    v = (g - a * u) // b  # Compute v from the equation au + bv = g
    return g, u, v

def sum_table_integers_modulo(n):
    table = {}
    for i in range(n): 
        for j in range(n):
            x = (i + j) % n
            table[(i,j)] = x
    return table

def table_group_of_units(n):

    units = []
    for i in range(1, n):
        if extended_gcd(i, n)[0] == 1:
            units.append(i)

    table = {(a, b): (a * b) % n for a in units for b in units}

     # Display using pandas DataFrame
    df = pd.DataFrame([[table[(a, b)] for b in units] for a in units],
                      index=[f"{a}" for a in units],
                      columns=[f"{b}" for b in units])

    df.index.name = "×"
    return df


def square_and_multiply_mod(N, g, A):
    a = g
    b = 1
    while A > 0:
        if A % 2 == 1:
            b = (b * a) % N
        a = (a ** 2) % N
        A = A // 2
    return b

def primitive_root_test(g: int, p: int) -> bool:
    """
    Return True iff g is a primitive root modulo the *prime* p,
    using the 'more-than-half-the-residues' shortcut.
    """
    if g % p == 0:
        return False                    # 0 can never be a primitive root

    seen = set()
    needed = (p - 1) // 2 + 1           # one past half of p-1

    # Skip exponent 0 (g**0 ≡ 1) so we don't waste a slot on 1
    for A in range(1, needed + 1):      # exponents 1 … needed
        power = square_and_multiply_mod(p, g, A)
        if power in seen:               # repeat → order ≤ A ≤ (p-1)/2
            return False
        seen.add(power)

    # If we got this far without repeats, order > (p-1)/2 ⇒ order = p-1
    return True

# This code is not optimal, but we are recycling the previous function. 