#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fractions
from functools import reduce

def lcm(a, b): return int(a * b / fractions.gcd(a, b)) if a and b else 0

def p5(n):
    return reduce(lambda x, y:
                  lcm(x, y),
                  [ x for x in range(1, n + 1) ])

def main():
    print(p5(20))

if __name__ == '__main__':
    main()
