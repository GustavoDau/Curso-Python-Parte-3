#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome:')))
    temp.append(int(input('Peso')))
    if len(princ) == 0:
        mai = men = temp[1] # 1 porque se refere ao peso, 0 eh o nome da pessoa
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? S/N')).upper()
    if resp == 'N':
        break
print(f'ao todo voce cadastrou {len(princ)} pessoas')
for p in princ:
    if p[1] == mai:
        print(f'a pessoa {p[0]} teve o maior peso  de {mai}Kg')
    if p[1] == men:
        print(f'a pessoa {p[0]} teve o menor peso  de {men}Kg')