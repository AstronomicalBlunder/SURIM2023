"""
File contains code to print a list of exponents over a given prime and print it iff it's supersingular, and what class of supersingular
surface it falls under.

"""

import cProfile
import gc
import itertools
import signal

import numpy as np

from glob              import glob
from main              import run_affine, run_projective
from newton_polygons   import *
from plot              import plot_lines, plot_multiple_lines
from rational_function import *
from sage.all          import *
from smooth            import my_WP_smooth
from supersingular     import *
from time              import time
from variety           import AffineVariety, DefiningEquation, ProjectiveVariety


def print_result(exponents, q):
    coeffs = [1]*len(N)
    variety = AffineVariety(q, DefiningEquation(coeffs, exponents))
    #Only print supersingular varieties (i.e the one's we're interested in)
    if(variety.is_supersingular()):
        string = "IN A NEW CLASS"
        ##If S.S variety is in a class we already know then say that
        if(gcd_condition(exponents)):
            string = "GCD_OBVIOUS"
        elif(len(exponents) == 4 and ben_form1(exponents, q)):
            string = "BEN_FORM_ONE"

        print(exponents,  ": ", string)


##Check basic gcd condition
def gcd_condition(N):
    for i in range(len(N)):
        coprime = True
        for j in range(len(N)):
            if i != j and gcd(N[i], N[j]) != 1:
                coprime = False
        if coprime:
            return True
    return False

#Check if a is primitive root mod n
def is_primitive_root(a, n):
    order = Mod(a, n).multiplicative_order()
    return order == euler_phi(n)


#Check if a given surface with exponents N is of the form found by Ben over F_w
#Assumes input is a surface in P^3
def ben_form1(N, w):
    N = sorted(N)
    p, q = N[0], N[1]
    if(is_prime(p) and is_prime(q)):
        s = N[2]/p
        if(isinstance(s, int) and s == N[3]/q):
            if([p%s, q%s, w%s] == [1, 1, 1]):
                if(is_primitive_root(w, p) and is_primitive_root(w, q)):
                    return True
    return False


#Checks if the given surface with exponents N is of the form w^abc + x^a + y^b + z^c that was found by Ben over F_p
#Assume input is a surface over P^3
##CODE IS CURRENTLY NOT WORKING
"""
def ben_form2(N, p):
    N = sorted(N)
    a, b, c = N[0], N[1], N[3];
    if(!is_prime(a) or !is_prime(b) or !is_prime(c)):
             return False;
    f1 = Mod(p, a).multiplicative_order();
    f2 = Mod(p, b).multiplicative_order();
    f3 = Mod(p, c).multiplicative_order();
    flist = [f1, f2, f3];
    v = ZZ.valuation(2);
    r = v(f_1);
    s = v(f_2);
    t = v(f_3);
    val_list = [r, s, t];
    if(s != 2):
        return False;
    if(t != 2):
        return False;
    if(r <= 2):
        return False:
    if(f1 != a - 1):
        return False:
    if(f2 != b - 1):
        return False:
    if(f3 != c - 1):
        return False:
    for i in range(len(flist)):
       for j in range(len(flist)):
             if i != j:
                 x = flist[i]/(2^val_list[i]);
                 y = flist[j]/(2^val_list[j]);
                 if (gcd(x, y)!= 1):
                     return False;
    condition1 = False;
    x = (a - 1)*(c - 1);
    for i in range(x):
        if isinstance(x/i, Int):
             if p^i % ac == b:
                 condition1 = True;
    if !condition1:
       return False;
    condition2 = False;
    y = (a - 1)*(b - 1);
    for j in range(y):
        if isinstance(y/j, Int):
             if p^j % ab == c:
                 condition2 = True;
    if !condtion2:
       return False;
    return True;
"""

q = 19
n3 = 4
n = 20
for n2 in range(1, n):
    for n1 in range(1, n):
        N = [n1, n2, n3]
        print_result(N, q)

