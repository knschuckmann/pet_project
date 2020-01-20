import pytest

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from TicTacToe_Game import TicTacToeGame

# class object creation
game_obj = TicTacToeGame()

def test_init_board():
    assert game_obj.get_board().all() == ' ', 'Should be \' \' '

def test_init_turn():
    assert game_obj.get_turn() == ['computer', 'player'], 'Should be [\'computer\', \'player\'] '

def test_init_choosen_letter():
    assert game_obj.get_choosen_letter() == ['X', 'O'], 'Should be [\'X\', \'O\'] '

def test_init_choosen_game_flag():
    assert game_obj.get_game_flag() == 'nothing', 'Should be \'nothing\' '
   
def test_set_turn():
    assert game_obj.turn.reverse() == game_obj.set_turn(False), 'Should be [\'player\', \'computer\'] '

