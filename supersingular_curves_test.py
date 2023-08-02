from cocalc_code import *
from sage.arith.functions import LCM_list


nPrimes = 9;

# Generate Q, the list of the first nPrimes
P = Primes();
Q = []; i = 0;
while i < nPrimes:
    Q.append(P.unrank(i));
    i = i + 1;

sols = [];

#def primitiveRoot(p, q, w):
#    return Mod(w,p).multiplicative_order() == p-1 and Mod(w,q).multiplicative_order() == q-1;

#def wCondition(p, q, w):
#    for v in range((p-1)*(q-1)):
#        if (w**v + 1) % p*q == 0:
#            return True;
#    return False;

#def sCondition(p, q, w, s):
#    if (p - 1) % s == 0 and (q - 1) % s == 0 and (w - 1) % s == 0:
#        return True;
#    return False;
    
# Generate a list of varieties to check supersingularity for
for p in range(1, 20):
    for q in range(p, 20):
        for r in range(q, 20):
            for w in Q:
                N = (p, q, r);
                if primitiveExp(N) and gcd(N) == 1 and (N, w) not in sols and not isTrivial(N, w) and not singular(N, w):
                    sols.append((N, w));
                
print(len(sols), "possible varieties\n");
count = 0;

# Print the supersingular varieties from the list generated above
for sol in sols:
    N = sol[0];
    w = sol[1]
    
    if supersingular(N, w):
        print(sol);
        count += 1;
        

print(count, "supersingular varieties");
