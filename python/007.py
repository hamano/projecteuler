#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isPrime(n, primes):
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

def p7(max):
    primes = [2, 3, 5]
    i=1
    while len(primes) < max:
        p = 6 * i + 1
        if isPrime(p, primes):
            primes.append(p)
        p += 4
        if isPrime(p, primes):
            primes.append(p)
        i+=1
    return primes.pop()

def main():
    print(p7(10001))

if __name__ == '__main__':
    main()
