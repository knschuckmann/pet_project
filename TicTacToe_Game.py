#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:50:15 2020
test e

@author: Kostja
"""
import numpy as np
import random
import copy

class TicTacToe_Game(object):
    ####################### CONSTRUCTOR #######################
    def __init__(self):
        self.board = self.reset_board() 
        self.turn = ['computer', 'player']
        self.choosen_letter = ['X', 'O']
        self.game_flag = 'nothing'
        self.__possible_moves = {'1': (0,0), '2': (0,1), '3': (0,2), '4': (1,0), '5': (1,1), '6': (1,2), '7': (2,0), '8': (2,1), '9': (2,2)}

    ####################### GETTER AND SETTER #############################      
    
    # set board to reset 
    def reset_board(self):
        return np.full((3, 3),' ', dtype="object") 
    
    # get board
    def get_board(self):
        return self.board
    
    # set upcomming turn 
    def set_turn(self, reverse = False):
        if reverse == True:
            self.turn.reverse()
        else:
            self.turn = ['computer','player']
            
    # get current turn
    def get_turn(self):
        return self.turn
    
    # set letter
    def set_choosen_letter(self, reverse = False):
        if reverse == True:
            self.choosen_letter.reverse()
        else:
            self.choosen_letter = ['X','O']
        
    # get choosen letter
    def get_choosen_letter(self):
        return self.choosen_letter
    
    # set game flag
    def __set_game_flag(self, string):
        self.game_flag = string
    
    # get game flag
    def get_game_flag(self):
        return self.game_flag

    ####################### METHODS ####################### 
    
    # whos turn is it and decide which letter player has
    def turn_and_letter_decission(self,):
        # Randomly choose the player who goes first.
        # first in list is toss winner
        if random.randint(0,1)  == 1:
            self.set_turn(reverse = True)
        
        # Lets the player type which letter they want to be.
        # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
        player_letter = ''
        while not (player_letter == 'X' or player_letter == 'O'):
            print('Do you want to be X or O?')    
            player_letter = input().upper()
    
        # the first element in the list is the player’s letter, the second is the computer's letter.    
        if player_letter == 'X':  
            self.set_choosen_letter()
        else:    
            self.set_choosen_letter(reverse = True)
            
        return [self.get_choosen_letter(), self.get_turn()] 
    
    
    # make move on Board
    def makeMove(self, letter, board, move):
        if move in self.__possible_moves:
            board[self.__possible_moves[move]] = letter
       
    # draw the board to see the results
    def drawboard(self, board): 
        # This function prints out the board that it was passed.
        # "board" is a list of strings representing the board (ignore index  0)
        print('   |   |')
        print(' ' + board[self.__possible_moves['7']] + ' | ' + board[self.__possible_moves['8']] + ' | ' + board[self.__possible_moves['9']])  
        print('   |   |')      
        print('-----------')      
        print('   |   |')      
        print(' ' + board[self.__possible_moves['4']] + ' | ' + board[self.__possible_moves['5']] + ' | ' + board[self.__possible_moves['6']])      
        print('   |   |')      
        print('-----------')      
        print('   |   |')      
        print(' ' + board[self.__possible_moves['1']] + ' | ' + board[self.__possible_moves['2']] + ' | ' + board[self.__possible_moves['3']])      
        print('   |   |')
    
    def reset(self):
        self.board = self.reset_board()
        self.set_choosen_letter()
        self.set_turn()
        self.__set_game_flag('nothing')
    
    
    def getPlayerMove(self, board):
        # Let the player type in their move.    
        move = ' '    
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.__isSpaceFree(move, board):   
            print('What is your next move?(1-9) \n\nBotom left is 1 and top right is 9')    
            move = input()
            
        return str(move)
    
    def __isSpaceFree(self, move, board):
        # Return true if the passed move is free on the passed board.    
        return board[self.__possible_moves[move]] == ' '
    

       
    def __isWinner(self, letter, board):
        # Given a board and a player’s letter, this function returns True if that player has won.   
        # We use bo instead of board and le instead of letter so we don’t have to type as much.
        return ((board[self.__possible_moves['7']] == letter and board[self.__possible_moves['8']] == letter and board[self.__possible_moves['9']] == letter) or # across the top                                            
        (board[self.__possible_moves['4']] == letter and board[self.__possible_moves['5']] == letter and board[self.__possible_moves['6']] == letter) or # across the middle
        (board[self.__possible_moves['1']] == letter and board[self.__possible_moves['2']] == letter and board[self.__possible_moves['3']] == letter) or # across the bottom    
        (board[self.__possible_moves['7']] == letter and board[self.__possible_moves['4']] == letter and board[self.__possible_moves['1']] == letter) or # down the left side    
        (board[self.__possible_moves['8']] == letter and board[self.__possible_moves['5']] == letter and board[self.__possible_moves['2']] == letter) or # down the middle    
        (board[self.__possible_moves['9']] == letter and board[self.__possible_moves['6']] == letter and board[self.__possible_moves['3']] == letter) or # down the right side    
        (board[self.__possible_moves['7']] == letter and board[self.__possible_moves['5']] == letter and board[self.__possible_moves['3']] == letter) or # diagonal    
        (board[self.__possible_moves['9']] == letter and board[self.__possible_moves['5']] == letter and board[self.__possible_moves['1']] == letter)) # diagonal

    
    def determine_winner_or_tie(self, letter, board):       
        if self.__isWinner(letter, board):
            self.drawboard(board)
            if self.get_turn()[0] == 'player' :
                print('Hooray! You have won the game!') 
            else:
                print('The computer has beaten you! You lose.')   
            return self.__set_game_flag('winner')
        else:
            if ' ' not in board:    
                self.drawboard(board)   
                print('The game is a tie!') 
                self.__set_game_flag('tie')
            else:    
                self.set_turn(reverse = True)
                
        #return self.get_game_flag()
    
    
    def getComputerMove(self, board):
     
        playerLetter, computerLetter = self.get_choosen_letter()
        
        # Here is our algorithm for our Tic Tac Toe AI:    
        # First, check if someone can win in the next move 
        for i in range(1,10):
            board_copy = copy.copy(board)
            if self.__isSpaceFree(str(i), board_copy ):
                for j,letter in enumerate(self.get_choosen_letter()):
                    self.makeMove(letter, board_copy, str(i))    
                    if self.__isWinner(letter, board_copy):
                        return str(i)
            
        # Try to take one of the corners, if they are free. 
        for i, numb in enumerate('1 3 7 9'.split()):
            move = self.__isSpaceFree(numb, board)    
            if move == True:    
                return numb
                    
        # Try to take the center, if it is free.    
        if self.__isSpaceFree('5'):    
            return '5'    
            
        # Move on one of the sides.    
        for i, numb in enumerate('2 4 6 8'.split()):
            move[i] = self.__isSpaceFree(numb, board)  
        return random.choice(move)

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        self.reset()
        return input().lower().startswith('y')

