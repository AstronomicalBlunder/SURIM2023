from sage.all import *
from sage.arith.functions import LCM_list

# Calculate relevant s-function in Stickleberger's thm
def s(v, p, f):
    q = p**f;
    return (p-1) * sum([frac(p**i * v) for i in range(0, f)])


# Check modulo condition for L-tuples
def condition(l, N, n, r):
    for j in range(0, r + 1):
        if (l[j] * N[j]) % n != 0:
            return False;
    return True;

# Check if covered by supersingular fermat
def fermatCover(N, p):
    n = LCM_list(N);
    for v in range(euler_phi(n)):
        if power_mod(p, v, n) == Mod(-1, n):
            return True;
    return False;

# Check if one exponent is coprime to the rest
def gcdCondition(N):
    for i in range(len(N)):
        coprime = True;
        for j in range(len(N)):
            if i != j and gcd(N[i], N[j]) != 1:
                coprime = False;
        if coprime:
            return True;
    return False;

# Check if of the form 2a, 2b, 2c for a,b,c pairwise coprime
def quadricCondition(N):
    if len(N) == 3:
        if N[0] % 2 == 0 and N[1] % 2 == 0 and N[2] % 2 == 0:
            a = N[0]/2; b = N[1]/2; c = N[2]/2;
            if gcd(a,b) == 1 and gcd(a,c) == 1 and gcd(b,c) == 1:
                return True;
    return False;

# Check if the curve is singular
def singular(N, p):
    for i in range(len(N)):
        if N[i] % p == 0:
            return True;
    return False;

# Exclude cases we don't care about
def isTrivial(N, p):
    if gcdCondition(N) or quadricCondition(N):
        return True;
    return False;


#Returns if a diagonal hypersurface with exponent list N is superingular over F_p
def supersingular(N, p):
    if isTrivial(N, p):
        return True;
    r = len(N) - 1;
    n = LCM_list(N);
    f = Mod(p, n).multiplicative_order();
    q = p**f;
    # Create list of tuples {L_0,...L_r} to iterate over
    n_set = [i for i in range(1, n)];
    L0 = Tuples(n_set, r + 1);
    L = [l for l in L0 if (sum(l) % n == 0 and condition(l, N, n, r))];
    # Check condition for each tuple
    value = (r+1)/2 * (p-1) * f;
    for l in L:
        for m in [i for i in range(1, n) if gcd(i, n) == 1]:
            if sum([s(m * l[i] / n, p, f) for i in range(0, r + 1)]) != value:
                return False;
    return True;
