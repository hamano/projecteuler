#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def p9(n):
    return list(map(
        lambda l: l[0] * l[1] * l[2],
        filter(
            lambda l: l[0] * l[0] + l[1] * l[1] == l[2] * l[2],
            [ (a, b, n - a - b)
              for a in range(1, int(n / 3)) for b in range(a, int(n / 2)) ])))

def main():
    print(p9(1000))

if __name__ == '__main__':
    main()
