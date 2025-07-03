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
