#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 18:25:30 2021

@author: amitavchrismostafa
"""

age_str = input()
try:
    age = int(age_str)
except ValueError:
    print('tough luck')
