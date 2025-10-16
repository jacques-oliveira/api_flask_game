#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 16:29:09 2025

@author: jacques
"""

from flask import Flask, jsonify, render_template
from Cliente import Cliente
from ObjetoClasse import ObjetoClasse
#%%
app = Flask(__name__)
cliente = Cliente()

@app.route('/')
def home():
    return 'hellow world'

@app.route('/dados')
def obter_dados():
    dados = cliente.list_objects()
    return jsonify([{'title': g.title, 'image': g.image} for g in dados])

def exibir_conteudo():
    dados = cliente.list_objects()
    return render_template(dados.html, dados = dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port= 8080, debug = True)