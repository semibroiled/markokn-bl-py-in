#!/usr/bin/env python3.
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:46:54 2021

@author: amitavchrismostafa
"""

if __name__ == '__main__':
    print(f'the current module is being run and not imported')
else:
    print(__name__)


def square(a):
    '''Returns the squared of a number '''
    try:
        a = int(a)
        return a*a
    except ValueError as e:
        print('Could not parse input as number')
        print(e, e.args)


while True:
    b = input('Enter a number:\n')
    print(square(b))
    x = input('Continue? Press Enter')
    if x:
        break
