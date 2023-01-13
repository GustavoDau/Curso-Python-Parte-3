#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
# – Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)

def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media']>=7:
            r['situacao'] = 'boa'
        elif r['media']>=5:
            r['situacao'] = 'razoavel'
        else:
            r['situacao'] = 'razoavel'
    return r


resp = notas(9, 10, 5,5, 2,5, 8, sit=True)
print(resp)

num = [3, 6, 4, 1]
for a, b in enumerate(num):
    print(a + b)