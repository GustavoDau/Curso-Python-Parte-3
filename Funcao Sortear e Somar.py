# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 10 valores ', end='')
    for c in range(0, 10):
        n = randint(1, 50)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)


def soma(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de{lista} temos {soma}')


numeros = list()
sorteia(numeros)
soma(numeros)