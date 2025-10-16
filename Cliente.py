#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 16:20:42 2025

@author: jacques
"""
from ObjetoClasse import ObjetoClasse
import requests
#%%
class Cliente:
    def __init__(self):
        self.url = 'https://www.gamerpower.com/api'
    
    def list_objects(self):
        response = requests.get(self.url+'/giveaways')
        if response.status_code == 200:
            data = response.json()
            return [ObjetoClasse(item) for item in data]
        return []