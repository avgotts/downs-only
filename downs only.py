# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:44:21 2019

@author: Sargon
"""

import puz # https://github.com/alexdej/puzpy
from collections import defaultdict

pzzle = "aaaaaa.puz"
# default puzzle for testing. NYT puzzle from June 2018 that I renamed
  
def downs(puzzle=pzzle):
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
    p.save("downss.puz")
    
    