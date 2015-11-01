#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def div_count(n):
    i=2
    c=1
    while i * i <= n:
        j=1
        while n % i == 0:
            n /= i
            j+=1
        i+=1
        c*=j
    if 1 < n:
        return c * 2
    else:
        return c

def p12():
    n=1
    while True:
        tri = n * (n + 1) / 2
        c = div_count(tri)
        if c > 500:
            return tri
        n+=1

def main():
    print(p12())

if __name__ == '__main__':
    main()
