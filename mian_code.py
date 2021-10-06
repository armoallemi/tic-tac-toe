# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 03:54:08 2021

@author: moallemi_a
"""
import xo_functions as xo
import os


# the follwowing code runs the XO game and keep asking for replay after each 
# round of game

def main():
        
    replay_cond = True
    
    while replay_cond:
    
         xo.play_game()
         replay_cond = xo.replay()


if __name__ == '__main__':
    main()    