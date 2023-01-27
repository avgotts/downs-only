# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:44:21 2019

@author: Sargon
"""

import puz # https://github.com/alexdej/puzpy
from collections import defaultdict
import fnmatch
import os


  
def downs(puzzle):
    p = puz.read(puzzle)
    n = p.clue_numbering()
    d = defaultdict(int)
    #this next chunk gets an ordering for the clues
    #in p.clues, they go 1a, 1d, 2d, 3d, 4d, 5a, 5d, etc.
    for clue in n.across:
        d[clue["num"]]+=1
    for clue in n.down:
        d[clue["num"]]+=1
    last_clue = n.across[-1]["num"]
    #this chunk is to identify all of the across clues so they can be replaced
    #1a is always first, hence the initial conditions for clue_num
    clue_num = {1:0}
    for i in range(2, last_clue + 1):
        clue_num[i] = clue_num[i-1]+d[i-1]
    #this does the replacing. clue_num takes the number of the clue and
    #returns the position of the clue in the overall list (p.clues)
    for clue in n.across:
        j = clue["num"]
        p.clues[clue_num[j]] = "-"
    p.save("downs" + puzzle[:-4]+".puz")
    
def d_all():
    #converts all the .puz files in the directory to downs-only
    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.puz"):
            downs(file)
            
if  __name__ == "__main__":
    d_all()