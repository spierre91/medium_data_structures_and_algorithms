#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:52:32 2020

@author: sadrachpierre
"""
medical_charges = ["500", "1000", None , "450", "230", None]
print(medical_charges)


medical_charges = [n for n in medical_charges if n != None]
print(medical_charges)

medical_charges = [int(n) for n in medical_charges if n != None]
print(medical_charges)


charges = (int(n) for n in medical_charges if n != None)
print(charges)

for charge in charges:
    print(charge)
    
    
def convert_and_filter(input_list):
    try:
        int(input_list)
        return True
    except ValueError:
        return False
    
charges = list(filter(convert_and_filter, medical_charges))
print(charges)