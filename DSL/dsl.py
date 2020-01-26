#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:55:36 2020

@author: Kostja
"""
import sys
import importlib

# The source file is the 1st argument to the script
if len(sys.argv) != 2:
    print('usage: %s <src.dsl>' % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()
        print(parts)

        mod = importlib.import_module(parts[0])
        getattr(mod, parts[1])(parts[2], parts[3])
        print(mod)