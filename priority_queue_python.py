#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:11:18 2020

@author: sadrachpierre
"""

import heapq

ibm_prices = [108.68, 109.65, 121.01, 122.78, 120.16]

print(heapq.nsmallest(3, ibm_prices))

print(heapq.nlargest(3, ibm_prices))

portfolio = [
       {'name': 'IBM', 'shares': 200, 'price': 108.68},
       {'name': 'AAPL', 'shares': 75, 'price': 277.97},
       {'name': 'FB', 'shares': 40, 'price': 170.28},
       {'name': 'HPQ', 'shares':125, 'price': 17.18},
       {'name': 'UBER', 'shares': 50, 'price': 22.60},
       {'name': 'TWTR', 'shares': 95, 'price': 29.29}
]


cheap_stocks = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive_stocks = heapq.nlargest(3, portfolio, key=lambda s: s['price'])


print("Cheap Stocks: ", cheap_stocks)
print("Expensive Stocks: ", expensive_stocks)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        
    def is_empty(self):
        return not self._queue 
        
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Stock:
    def __init__(self, stock_ticker, stock_price, stock_share):
        self.stock_ticker = stock_ticker
        self.stock_price = stock_price
        self.stock_share = stock_share 
    def __repr__(self):
        return 'Stock({}, {}, {})'.format(self.stock_ticker , self.stock_price,  self.stock_share)
    
        
        

q = PriorityQueue()

q.push(Stock('IBM', 108.68, 200), 6)
q.push(Stock('HPQ', 17.18, 125), 1)
q.push(Stock('TWTR', 29.29, 95), 3)
q.push(Stock('UBER', 22.6, 50), 2)
q.push(Stock('AAPL', 277.97, 75), 4)
q.push(Stock('FB', 170.28, 40), 4)

while not q.is_empty():
    print(q.pop())