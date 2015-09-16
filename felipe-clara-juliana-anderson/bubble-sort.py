from __future__ import print_function
N=20 #quantidade de números que tem na lista
lista=[11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 4, 17, 9, 13, 7, 10, 15, 2, 8] #números dispostos aleatoriamente na lista
print("Lista original:", lista) #imprime a lista original, com os números dispostos da forma aleatoria
for i in range(0, N - 2, 1): #a posição começa no zero e vai a 18, de um em um
    for j in range(i + 1, N - 1, 1): #a posição vai de i+1 a 19, de um em um
        if lista[i]>lista[j]: #se a lista i for maior que a lista j, segue-se:
            tmp=lista[i] #procedimento usado para trocar os elementos de lugar
            lista[i]=lista[j] #procedimento usado para trocar os elementos de lugar
            lista[j]=tmp #procedimento usado para trocar os elementos de lugar
print("Lista crescente:", lista) #imprime a lista crescente, com os números em ordem crescente