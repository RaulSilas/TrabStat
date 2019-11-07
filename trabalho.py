import time
# Declaração de variáveis
listaMat = []
listaFis = []
xy = 0
yi = 0
xi = 0
xiQuad = 0
yiQuad = 0
parte1 = 0
parte2 = 0
raizQ = 0
parte3 = 0
a = 0
b = 0
mediaX = 0
mediaY = 0
help1 = 0
help2 = 0
help3 = 0

n = int(input("Digite a quantidade de linhas para cada tabela: "))

def coletarvalores():
    lista = []
    print("--------------------------------------------------------")
    print("")

    for i in range(1, n + 1):

        while True:
            try:
                aux = input("Digite o " + str(i) + "º Valor: ")
                if aux.isdigit():
                    lista.append(float((aux)))
                else:
                    raise ValueError("Valor fora do range permitido")
            except ValueError as e:
                print("Valor inválido:", e)
            else:
                break

    return lista

listaMat = coletarvalores()
listaFis = coletarvalores()

## Multiplicando x * y e somando

def somaxy(primLista, segLista):
    aux = 0
    for i in range(0, n):
        aux += primLista[i] * segLista[i]
    return aux

xy = somaxy(listaMat, listaFis)

## Somando os valores da primeira tabela

def somaxi(primLista):
    aux = 0
    for i in range(0, n):
        aux += primLista[i]
    return aux

xi = somaxi(listaMat)

## Somando os valores da segunda tabela

def somayi(segLista):
    aux = 0
    for i in range(0, n):
        aux += segLista[i]
    return aux

yi = somayi(listaFis)

## Somando os valores ao quadrado da primeira tabela

def quadxi(primLista):
    aux = 0
    for i in range(0, n):
        aux += primLista[i] ** 2
    return aux

xiQuad = quadxi(listaMat)

## Somando os valores ao quadrado da segunda tabela

def quadyi(segLista):
    aux = 0
    for i in range(0, n):
        aux += segLista[i] ** 2
    return aux

yiQuad = quadyi(listaFis)

#########################################################################################################
##### Segunda Parte #####

parte1 = (n * xy) - (xi * yi)
parte2 = (n * xiQuad - (xi ** 2)) * (n * yiQuad - (yi ** 2))
raizQ = parte2 ** (1/2)
parte3 = parte1/raizQ
parte3 = round(parte3, 4)

print("")
print("-----------------------------------------------------------------")
print("------------------- Resultados Correlação -----------------------")
print("-----------------------------------------------------------------")
print("")
print("Soma de x * y: " + str(xy))
print("Soma dos valores da primeira tabela: " + str(xi))
print("Soma dos valores da segunda tabela: " + str(yi))
print("Soma de X elevado ao quadrado: " + str(xiQuad))
print("Soma de X elevado ao quadrado: " + str(yiQuad))
print("Coeficiente de correlação de Pearson: " + str(parte3))
print("")

time.sleep(10)

help1 = (n * xy) - (xi * yi)
help2 = n * xiQuad - (xi ** 2)

a = help1 / help2

mediaX = xi / n
mediaY = yi / n

b = mediaY - a * mediaX
b = round(b, 4)


print("")
print("-----------------------------------------------------------------")
print("--------------------- Resultados Regressão ----------------------")
print("-----------------------------------------------------------------")
print("")
print("a = " + str(a))
print("Média de X = " + str(mediaX))
print("Média de Y = " + str(mediaY))
print("b = " + str(b))
print("")
print("Portanto: Y = " + str(b) + "X + " + str(a))
print("")

time.sleep(10)

def estimar():
    while True:
        try:
            valor = input("Digite o Valor: ")
            if valor.isdigit():
                res = (b + a * float(valor))
                print("Resultado do valor estimado: " + str(res))
                time.sleep(10)
            else:
                raise ValueError("Valor fora do range permitido")
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            break

chave = True
exit = 0

##Estrutura para caso o usuário queira estimar um valor fora da lista inicial.
while(chave):

    print("Deseja estimar um valor?")
    exit = input("DIGITE UMA LETRA PARA CANCELAR!")
    if exit.isdigit():
        estimar()
    else:
        break
