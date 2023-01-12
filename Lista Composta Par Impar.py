#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
valores = 0
for n in range(0, 7):
    valores =(int(input('Entre com um numero')))
    if valores % 2 == 0:
        lista[0].append(valores)
    else:
        lista[1].append(valores)
lista[0].sort()
lista[1].sort()
print(lista[0])
print(lista[1])