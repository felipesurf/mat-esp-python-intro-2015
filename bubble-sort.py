import matplotlib.pyplot as plt
N=20 #quantidade de números que tem na lista
lista=[11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] #números dispostos aleatoriamente na lista
print("Lista original:", lista) #imprime a lista original, com os números dispostos da forma aleatoria
plt.figure()
plt.plot(range(0,N, 1),lista, "ok")
plt.title("Lista Original")
plt.xlabel("Índices")
plt.ylabel("Números")
plt.savefig("fig/bubble-inicio.png") 
plt.close()
numtroca=0
iteracao=0
for i in range(0, N - 1, 1): #a posição começa no zero e vai a 18, de um em um
    for j in range(i + 1, N , 1): #a posição vai de i+1 a 19, de um em um
        plt.figure()
        plt.plot(range(0,N, 1),lista, "ok")
        plt.title("Lista em ordem crescente")
        plt.ylabel("Números")
        plt.plot(lista[i],lista,'or')
        plt.plot(lista[j],lista,'ob')
        plt.savefig("fig/bubble-it-{}.png".format(iteracao)
        plt.close()
        if lista[i]>lista[j]: #se a lista i for maior que a lista j, segue-se:
            tmp=lista[i] #procedimento usado para trocar os elementos de lugar
            lista[i]=lista[j] #procedimento usado para trocar os elementos de lugar
            lista[j]=tmp #procedimento usado para trocar os elementos de lugar
            numtroca=numtroca + 1 
            plt.figure()
            plt.plot(range(0,N, 1),lista, "ok")
            plt.title("Lista em ordem crescente")
            plt.ylabel("Números")
            plt.savefig("fig/bubble-troca-{}.png".format(numtroca)) 
            plt.close()
print("Lista em ordem crescente:", lista) #imprime a lista crescente, com os números em ordem crescente
plt.figure()
plt.plot(range(0,N, 1),lista, "ok")
plt.title("Lista em ordem crescente")
plt.ylabel("Números")
plt.savefig("fig/bubble-fim.png") 
plt.close()
print("Cinco menores numeros:", lista[0:5]) #imprime os cinco menores números em da lista em ordem crecente
print("Cinco maiores numeros:", lista[N-5:N]) #imprime os conco maires números da lista em ordem crescente
