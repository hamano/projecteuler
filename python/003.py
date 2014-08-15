#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def factor(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(int(n))
    return factors

def p3(n):
    return max(factor(n))

def main():
    print(p3(600851475143))

if __name__ == '__main__':
    main()
