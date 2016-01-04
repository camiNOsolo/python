#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

empate = 0
ganado = 0
perdido = 0


def elige(x):
    return {
        '1': 'piedra',
        '2': 'papel',
        '3': 'tijeras',
        '5': 'salir',
    }.get(x, 'papel')


def eligeOpcion():
    print("Presiona 1 para Piedra")
    print("Presiona 2 para Papel")
    print("Presiona 3 para Tijeras")
    print("Presiona 5 para Salir")
    print("")

    eleccion = input("¿Que opcion eliges? ")

    resultado = elige(eleccion)

    if resultado == 'salir':
        print("")
        sys.exit('Saliendo del Juego...')
    else:
        return resultado


def computerEleccion():
    opciones = ["piedra", "papel", "tijeras"]
    opcionAleatoria = random.randint(0, 2)
    return opciones[opcionAleatoria]


def comparacion(humano, computer):
    if humano == computer:
        return "empate"
    if humano == "piedra" and computer == "papel":
        return "computer"
    if humano == "papel" and computer == "tijeras":
        return "computer"
    if humano == "tijeras" and computer == "piedra":
        return "computer"
    else:
        return "humano"

while True:
    humano = eligeOpcion()
    computer = computerEleccion()
    print("")
    print("Tu eleccion", humano)
    print("La eleccion de la computadora", computer)

    resultado = comparacion(humano, computer)

    if resultado == "empate":
        empate += 1

        if empate <= 1:
            print('Has empatado')
        else:
            print('Has empatado ' + str(empate) + ' veces')

    elif resultado == "computer":
        perdido += 1
        if perdido <= 1:
            print('Has perdido')
        else:
            print('Has perdido ' + str(perdido) + ' veces')
    else:
        ganado += 1
        if ganado <= 1:
            print('Has ganado')
        else:
            print('Has ganado ' + str(ganado) + ' veces')

    print("")
