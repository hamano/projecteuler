#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def p10(n):
    n+=1
    root = int(math.sqrt(n))
    l = list(range(n))
    l[0] = 0
    l[1] = 0
    for i in range(2, n):
        if l[i]:
            for j in range(i*2, n, i):
                l[j] = 0

    return sum(filter(lambda x: x != 0, l))

def main():
    print(p10(2000000))

if __name__ == '__main__':
    main()
