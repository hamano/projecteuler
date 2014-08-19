#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def powsum(n):
    return sum([int(math.pow(x, 2)) for x in range(1, n)])

def sumpow(n):
    return int(math.pow(sum([ x for x in range(1, n)]), 2))

def p6(n):
    return sumpow(n) - powsum(n)

def main():
    print(p6(100))

if __name__ == '__main__':
    main()
