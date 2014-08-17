#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def p4(n):
    return max(filter(lambda s: str(s) == str(s)[::-1],
                      [ x * y for x in range(1, n) for y in range(x, n) ]))

def main():
    print(p4(999))

if __name__ == '__main__':
    main()
