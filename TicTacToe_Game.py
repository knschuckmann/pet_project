#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:50:15 2020

@author: Kostja
"""
import numpy as np
import random

class TicTacToe_Game(object):
    def __init__(self):
        self.board = np.full((3, 3),' ', dtype="object") # empty board
        self.toss_winner = ''
        self.player_letter = ''
        
    def drawboard(self,board): 
        # This function prints out the board that it was passed.
        # "board" is a list of strings representing the board (ignore index  0)
        print('   |   |')
        print(' ' + board[2,0] + ' | ' + board[2,1] + ' | ' + board[2,2])  
        print('   |   |')      
        print('-----------')      
        print('   |   |')      
        print(' ' + board[1,0] + ' | ' + board[1,1] + ' | ' + board[1,2])      
        print('   |   |')      
        print('-----------')      
        print('   |   |')      
        print(' ' + board[0,0] + ' | ' + board[0,1] + ' | ' + board[0,2])      
        print('   |   |')
    
    def Toss_and_Letter(self,):
        # Randomly choose the player who goes first.
        if random.randint(0,1)  == 0:
            self.toss_winner = 'computer'
        else:
            self.toss_winner = 'player'
        
        # Lets the player type which letter they want to be.
        # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
        while not (self.player_letter == 'X' or self.player_letter == 'O'):
            print('Do you want to be X or O?')    
            self.player_letter = input().upper()
    
        # the first element in the list is the player’s letter, the second is the computer's letter.    
        if self.player_letter == 'X':    
            return ['X', 'O', self.toss_winner]    
        else:    
            return ['O', 'X', self.toss_winner]
    
    def resetBoard(self):
        self.board = np.full((3, 3),' ', dtype="object")
        
    def makeMove(self, board, letter, move):
        board[move] = letter
       
        
    
