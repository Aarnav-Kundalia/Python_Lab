import math
mass_electron = 9.11e-31           # electron mass (kg)
h_reduced = 1.054e-34       # reduced Planck constant (J·s)
eV = 1.6e-19 

well_depth_ev = 22.0
well_depth_joules = well_depth_ev * eV  
well_width = 1e-9

z0 = well_width * math.sqrt(2 * mass_electron * well_depth_joules) / h_reduced
print("z0 = ", z0)

def LHS_term(z):
    if z <= 0 or z >= z0:
        raise ValueError("z must be in the range (0, z0)")
    sqrt_term = (z0 / z) ** 2 - 1.0
    if sqrt_term < 0:
        raise ValueError("Square root term is negative, invalid z value")
    return math.sqrt(sqrt_term)

def f_even(z):
    s = LHS_term(z)
    if s is None:
        return None
    if abs(math.cos(z)) < 1e-10:
        return None
    return s - math.tan(z)

def f_odd(z):
    s = LHS_term(z)
    if s is None:
        return None
    if abs(math.sin(z)) < 1e-10:
        return None
    return s + 1.0 / math.tan(z)


def bisection(f, x1, x2, tol = 1e-19, max_iter = 300):
    f_left, f_right = f(x1), f(x2)
    if f_left == 0:
        return x1
    if f_right == 0:
        return x2
    if f_left * f_right > 0:
        raise ValueError("f(a) and f(b) should be of opposite sign")
    for i in range(max_iter):
        x3 = (x1 + x2)/2
        fm = f(x3)
        if fm is None:
            x3 += tol
            fm = f(x3)
            if fm is None:
                raise ValueError("Function evaluation failed at midpoint")
        if abs(fm) < tol or (x2 - x1)/2 < tol:
            return x3
        if f_left * fm < 0:
            x2, f_right =  x3, fm
        else:
            lower_limit, f_left = x3, fm
    return (lower_limit + x2)/2


def find_roots(func, zmin, zmax, steps=3000):
    roots = []
    dz = (zmax - zmin) / steps
    z_prev = zmin
    f_prev = func(z_prev)
    z = zmin + dz
    for i in range(steps):
        f_cur = func(z)
        if f_prev is not None and f_cur is not None and f_prev * f_cur < 0:
            root = bisection(func, z_prev, z, tol=1e-10, max_iter=300)
            if root is not None:
                if not any(abs(root - r) < 1e-7 for r in roots):
                    roots.append(root)
        z_prev = z
        f_prev = f_cur
        z += dz
        if z >= zmax:
            break
    return roots

even_roots = find_roots(f_even, 1e-8, z0)
odd_roots = find_roots(f_odd, 1e-8, z0)
print("z0 =", z0)
print("Even roots (z):", even_roots)
print("Odd roots (z):", odd_roots)


def energy_from_z(z):
    kconst2 = (z0**2 - z**2) / (well_width**2)
    Energy = - (h_reduced**2) * kconst2 / (2 * mass_electron)
    return Energy, Energy / eV


energies = []
for z in even_roots + odd_roots:
    EJ, EeV = energy_from_z(z)
    energies.append((z, EJ, EeV))
energies.sort(key=lambda x: x[1])
print("\nEnergies founnd (z, Energy in J, Energy in eV):")
for z, EJ, EeV in energies:
    print("z = {:.8f} , E = {:.6e} J , {:.6f} eV".format(z, EJ, EeV))
if not energies:
    print("No Energies found.")

