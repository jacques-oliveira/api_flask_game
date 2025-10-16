#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 16:29:09 2025

@author: jacques
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hellow world'
