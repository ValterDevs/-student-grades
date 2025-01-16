chave = []
valor = []

add = input('gostaria de adicionar alguma nota à algum aluno? sim/nao:')

while add == 'sim':
    add_outra_pessoa = str(input('digite o nome do aluno:'))
    add_outra_nota = str(input('digite a nota do aluno:'))
    chave.append(add_outra_pessoa)
    valor.append(add_outra_nota)
    add = input('gostaria de adicionar outra pessoa? sim/nao:')

dicion = list(zip(chave, valor))
dicion2 = dict(dicion)
print('esses são os resultados:', dicion2)
    


