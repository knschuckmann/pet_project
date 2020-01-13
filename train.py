#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 22:13:26 2020

@author: Kostja
"""
from Learn_TicTacToe import Learn_TicTacToe()


model = Learn_TicTacToe()



model()
def getComputerMove(board, computerLetter):
    
    
    # Given a board and the computer's letter, determine where to move and return that move.    
    if computerLetter == 'X':    
        playerLetter = 'O'
    else:
       playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:    
    # First, check if we can win in the next move    
    for i in range(1,10):
        copy = getBoardCopy(board)    
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)    
            if isWinner(copy, computerLetter):
                return i
        
    # Check if the player could win on their next move, and block them.    
    for i in range(1,10) :    
        copy = getBoardCopy(board)    
        if isSpaceFree(copy, i):    
            makeMove(copy, playerLetter, i)    
            if isWinner(copy, playerLetter):    
                return i    
        
    # Try to take one of the corners, if they are free.    
    move = chooseRandomMoveFromList(board, [1,3,7,9])    
    if move != None:    
        return move
            
    # Try to take the center, if it is free.    
    if isSpaceFree(board, 5):    
        return 5    
        
    # Move on one of the sides.    
    return chooseRandomMoveFromList(board, [2,4,6,8])