#numero de carnet 201404398
#numero a alcanzar para la secuencia 398
import os


def collatz(num):
    file = open("collatz.txt",a)
    N = num
    llenado = []
    for i in range (2, N):
        while i != 1:
            if i % == 0:
                llenado.append(i)
                i= i/2
            else:
                llenado.append(i)
                i=(i*3)+1
