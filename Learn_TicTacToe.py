#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:32:25 2020

@author: Kostja
"""
from torch import nn

class Learn_TicTacToe(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.forward = nn.Sequential(
            nn.Linear(18,9),
            nn.ReLU(True),
            nn.Dropout(p = 0.1),
            nn.Linear(9,1),
            nn.ReLU(True),
            nn.Dropout(p = 0.1)
            )
        

    def forward(self, x):
        x = self.forward(x)
        return x
    
    def name(self):
        return "LearnTicTacToe"
    
   