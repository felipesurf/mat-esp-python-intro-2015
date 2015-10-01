import matplotlib.pyplot as plt # importa a biblioteca para a criação de figuras
N=20 #quantidade de números que tem na lista
lista=[11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] #números dispostos aleatoriamente na lista
print("Lista original:", lista) #imprime a lista original, com os números dispostos da forma aleatoria
plt.figure() #cria uma figura
plt.plot(range(0,N, 1),lista, "ok")
plt.title("Lista Original")
plt.xlabel("Índices")
plt.ylabel("Números")
plt.savefig("fig/bubble-inicio.png") 
plt.close()
a=0
b=0
for i in range(0, N - 1, 1): #a posição começa no zero e vai a 18, de um em um
    for j in range(i + 1, N , 1): #a posição vai de i+1 a 19, de um em um
        b = b + 1
        plt.figure()
        plt.plot(range(0,N, 1),lista, "ok")
        plt.plot(i,lista[i], "or")
        plt.plot(j,lista[j], "ob") 
        plt.title("bubble-it{}".format(b))
        plt.xlabel("Índices")
        plt.ylabel("Números")
        plt.savefig("fig/bubble-it{}.png".format(b)) 
        plt.close()
        if lista[i]>lista[j]: #se a lista i for maior que a lista j, segue-se:
            tmp=lista[i] #procedimento usado para trocar os elementos de lugar
            lista[i]=lista[j] #procedimento usado para trocar os elementos de lugar
            lista[j]=tmp #procedimento usado para trocar os elementos de lugar
            a = a + 1
            plt.figure()
            plt.plot(range(0,N, 1),lista, "ok")
            plt.title("bubble-troca{}".format(a))
            plt.xlabel("Índices")
            plt.ylabel("Números")
            plt.savefig("fig/bubble-troca{}.png".format(a)) 
            plt.close()
print("Lista em ordem crescente:", lista) #imprime a lista crescente, com os números em ordem crescente
plt.figure()
plt.plot(range(0,N, 1),lista, "ok") 
plt.title("Lista em ordem crescente")
plt.xlabel("Índices")
plt.ylabel("Números")
plt.savefig("fig/bubble-fim.png") 
plt.close()
print("Cinco menores numeros:", lista[0:5]) #imprime os cinco menores números em da lista em ordem crecente
print("Cinco maiores numeros:", lista[N-5:N]) #imprime os conco maires números da lista em ordem crescente