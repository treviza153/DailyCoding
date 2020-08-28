#!/usr/local/bin python3

if __name__ == '__main__':

    lista = [10, 15, 3, 7, 6, 11]
    lista_saida = []
    k = 12

    for i in lista:
        if k - i in lista:
            lista_saida.append(i)

    print(lista_saida)