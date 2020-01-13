#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 23:02:01 2020

@author: Kostja
"""
from TicTacToe_Game import TicTacToe_Game

if __name__ == '__main__':
    tictactoe_game = TicTacToe_Game() # load game class
    print('Welcome to Tic Tac Toe!')
    while True:
        # Reset the board    
        theBoard = tictactoe_game.reset_board()
        
        letter , turn = tictactoe_game.turn_and_letter_decission()
 
        print('The ' + turn[0] + ' will go first.')    
        
        while tictactoe_game.get_game_flag() == 'nothing': 
            
            if turn[0] == 'player':    
                # Player’s turn.    
                tictactoe_game.drawboard(theBoard)    
                move = tictactoe_game.getPlayerMove(theBoard)    
                tictactoe_game.makeMove(letter[0], theBoard, move)
                tictactoe_game.determine_winner_or_tie(letter[0], theBoard)
            else:    
                # Computer’s turn.    
                move = tictactoe_game.getComputerMove(theBoard)    
                tictactoe_game.makeMove(letter[1], theBoard, move)
                tictactoe_game.determine_winner_or_tie(letter[1], theBoard)
                
        if not tictactoe_game.playAgain():   
            break