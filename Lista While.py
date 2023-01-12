#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
# já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
while True:
    n = int(input(' digite um numero'))
    if n not in valores:
        valores.append(n)
    else:
        print('nao podemos adicionar numeros repitidos')
    resp = str(input('voce gostaria de continuar? S/N')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'os numeros digitados foram {sorted(valores)}')