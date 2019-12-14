import math
import random
def to_binary(a):
	binary = []
	while a > 0:
		binary.append(a % 2)
		a = a//2
	binary.reverse()
	return binary

def modular_exponentiation(base,exponent,modulus):
	result = 1
	binary_exponent = to_binary(exponent)
	for i in range(len(binary_exponent)-1, -1, -1):
		if binary_exponent[i] == 1:
			result = (result*base) % modulus
		base *= base
	return result

def fermat_primality_test(p):
	if modular_exponentiation(2, p-1, p) == 1:
		return True
	return False

def prime_number_generator(length):
	x = 1
	primes = []
	while len(primes) < 2:
		x = random.randint(2**(length-1), 2**(length) - 1)
		if fermat_primality_test(x) == True:
			primes.append(x)
	return primes

def rGcd(m, n):
    print (m, n)
    if m % n == 0:
        return n
    else:
        gcd = rGcd(n, m % n)
        return gcd

def public_key(etval):
	while True:
		e = random.randint()
		if rGcd(e,etval) == 1:
			return e

def multiplicative_inverse(a, b):
    qi = [0,0]
    ri = [max(a,b), min(a,b)]
    si = [1,0]
    ti = [0,1]
    while(ri[-1] != 0):
        qi.append(ri[-2] // ri[-1])
        ri.append(ri[-2] % ri[-1])
        si.append(si[-2] - qi[-1]*si[-1])
        ti.append(ti[-2] - qi[-1]*ti[-1])
    return (ti[-2]+max(a,b)) % max(a,b)
    