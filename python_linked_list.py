#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:56:49 2020

@author: sadrachpierre
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None   
                        
   
class LinkedList: 
    def __init__(self):  
        
        self.head = None


    def printLinkedList(self): 
        value = self.head 
        while (value): 
            print(value.data) 
            value = value.next        
if __name__=='__main__':
    #initialize linked list object
    linkedlist = LinkedList()
    print(linkedlist)
    
    #assign values to nodes 
    linkedlist.head = Node('Speak to Me') 
    second = Node('Breathe') 
    third = Node('On the Run') 
    fourth = Node('Time') 
    fifth  = Node('The Great Gig in the Sky') 
    
    #link nodes
    linkedlist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    
    
    linkedlist.printLinkedList()