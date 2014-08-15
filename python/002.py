#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def fib_slow(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib_slow(n - 1) + fib_slow(n - 2)

def fib_gen(n):
    i = 1
    while True:
        x = fib_slow(i)
        if x > n:
            return
        yield x
        i += 1

def p2(n):
    return sum(filter(lambda x: x % 2 == 0, [ x for x in fib_gen(n) ]))

def main():
    print(p2(4000000))

if __name__ == '__main__':
    main()
