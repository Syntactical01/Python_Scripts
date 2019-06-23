# Given a max budget give the biggest quantity we can get for that budget
# Solution uses bisect's binary search

import sys
class Search():
    def __init__(self, get_cost):
        self.get_cost = get_cost
        self.length = 1
    
    def __getitem__(self, index): # index is the quantity
        self.length += 1
        print("Called", index)
        return self.get_cost(index)
        
    def __len__(self):
        """
        bisect uses len() as one of its first calls, so we will say
        the maximum quantity size will be the max int size for the
        system the script runs on.
        """
        return sys.maxsize

def get_cost(quantity):
    return quantity**2 + 3 * quantity + 100

budget = 1358841213

import bisect
max_quantity = bisect.bisect(Search(get_cost), budget) - 1

print(get_cost(max_quantity), budget, get_cost(max_quantity + 1))
