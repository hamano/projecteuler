#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def p1(n):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(n)))

def main():
    print(p1(1000))

if __name__ == '__main__':
    main()
