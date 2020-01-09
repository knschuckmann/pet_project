#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 23:02:01 2020

@author: Kostja
"""
from TicTacToe_Game import TicTacToe_Game

if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')
    
    tictactoe_game = TicTacToe_Game() # load game class
    while True:
        # Reset the board    
        theBoard = tictactoe_game.resetBoard()
        
        playerLetter, computerLetter, turn = tictactoe_game.Toss_and_Letter()
 
        print('The ' + turn + ' will go first.')    
        gameIsPlaying = True
        
        while gameIsPlaying:    
            if turn == 'player':    
                # Player’s turn.    
                tictactoe_game.drawBoard(theBoard)    
                move = getPlayerMove(theBoard)    
                makeMove(theBoard, playerLetter, move)    
        
                if isWinner(theBoard, playerLetter):    
                    drawBoard(theBoard)    
                    print('Hooray! You have won the game!')    
                    gameIsPlaying = False    
                else:    
                    if isBoardFull(theBoard):    
                        drawBoard(theBoard)    
                        print('The game is a tie!')    
                        break    
                    else:    
                        turn = 'computer'    
            else:    
                # Computer’s turn.    
                move = getComputerMove(theBoard, computerLetter)    
                makeMove(theBoard, computerLetter, move)    
        
                if isWinner(theBoard, computerLetter):    
                    drawBoard(theBoard)    
                    print('The computer has beaten you! You lose.')    
                    gameIsPlaying = False    
                else:    
                    if isBoardFull(theBoard):    
                        drawBoard(theBoard)    
                        print('The game is a tie!')    
                        break    
                    else:    
                        turn = 'player'    
        
        if not playAgain():    
            break
    