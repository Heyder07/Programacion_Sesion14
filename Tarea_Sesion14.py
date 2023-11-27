# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:50:02 2023

@author: heyde
"""

def operacion(a,b): #Push inicial
    if a > b:
        oper = a * b
        print(f'El resultado de la operación es {oper}')
    else:
        oper = a - b
        print(f'El resultado de la operación es {oper}')

operacion(300,20)