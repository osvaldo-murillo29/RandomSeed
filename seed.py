#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

semilla = input("Enter the seed: ")

numbers = []
for i in range(10):
    print '\nRESULT:', i

    random.seed(semilla)
    for sorteo in range(5):
        numbers = random.randint(0, 9)
        print numbers
