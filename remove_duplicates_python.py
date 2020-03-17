#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:16:04 2020

@author: sadrachpierre
"""

def remove_duplicates(items): 
    unique_items = set()
    for item in items:
        if item not in unique_items:
            yield item 
            unique_items.add(item)
            
emails = ['rob@gmail.com', 'mike@gmail.com',  'mike@gmail.com', 'sara@gmail.com',  'mike@gmail.com', 'fred@gmail.com']

print(list(remove_duplicates(emails)))

print(set(emails))
def remove_unhashable_duplicates(items, key=None): 
    unique_items = set()
    for item in items:
        val = item if key is None else key(item) 
        if val not in unique_items:
            yield item 
            unique_items.add(val)
            

patients = [{'name':'Rob Grant', 'medical_charges': 1500, 'medical_procedure': 'root canal'}, 
            {'name':'Sara Paulson', 'medical_charges':50000, 'medical_procedure':'cesarean section'},
            {'name':'Mike Cohen', 'medical_charges':26000, 'medical_procedure':'spinal fusion'},
            
            {'name':'Rob Grant', 'medical_charges': 1500, 'medical_procedure': 'root canal'}, 
            {'name':'Sara Paulson', 'medical_charges':50000, 'medical_procedure':'cesarean section'},
            {'name':'Mike Cohen', 'medical_charges':26000, 'medical_procedure':'spinal fusion'},
            
            {'name':'Jeff Goodwin', 'medical_charges': 3000, 'medical_procedure': 'cirumcision'}, 
            {'name':'Paul Johnson', 'medical_charges':49500, 'medical_procedure':'arthroplasty of knee'},
            {'name':'Grant Stein', 'medical_charges':32000, 'medical_procedure':'hip replacement'},]
            
print(list(remove_unhashable_duplicates(patients, key=lambda d: (d['name'],d['medical_charges'],d['medical_procedure']))))