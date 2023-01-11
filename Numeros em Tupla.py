#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

cont = 0

num = (int(input('digite um numero')),
      int(input('digite um numero')),
      int(input('digite um numero')),
      int(input('digite um numero')))



print(f'os numeros digitados foram {num}')
print(f'o numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o numero 3 apareceu na posicao {num.index(3) + 1}')
else:
    print(f'nao teve nenhum 3 digitado')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')