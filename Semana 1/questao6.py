#Função de Cadastrar Aluno
def cadastrarAluno(x):
  nome = input('Nome do aluno: ')
  return {'nome': nome, 'nota': 'Ainda não foi atribuida'}

#Função cadastrar nota do Aluno
def cadastrarNota(alunos, nome):
  num_de_alunos = len(alunos)
  for i in range(num_de_alunos):
    if nome == alunos[i]['nome']:
      nota = float(input(f'Digite a nota do aluno {nome}: '))
      alunos[i]['nota'] = nota
    else:
      print('Aluno não cadastrado\n')

#Função para consultar nome e nota de um aluno especifico
def consultarAluno(alunos, x):
  num_de_alunos = len(alunos)
  for i in range(num_de_alunos):
    if x == alunos[i]['nome']:
      print('Nome do Aluno: ', alunos[i]['nome'])
      print('Nota do Aluno:', alunos[i]['nota'], '\n')
      break
    else:
      print('Aluno não encontrado')

#Função que lista todos os nomes dos alunos cadastrados
def todosOsAlunos(alunos):
  num_de_alunos = len(alunos)
  for i in range(num_de_alunos):
    print(alunos[i]['nome'],'\n')
    print()

#Função para excluir alunos cadastrados
def excluirAluno(alunos, nome):
  num_de_alunos = len(alunos)
  for i in range(num_de_alunos):
    if nome == alunos[i]['nome']:
      del(alunos[i])
      break
    else:
      print('Aluno não encontrado')

#Sair do programa
def sair():
  return 'Fim do programa'

alunos = []         #Lista para armazenar os dados dos alunos

while(r != 0):
  print('\n1 - Cadastrar aluno\n2 - Cadastrar nota\n3 - Consultar Aluno\n4 - Todos os alunos\n5 - Excluir aluno\n0 - Sair')       #MENU
  r = int(input('Digite o respectivo numero da ação: '))                                                                          #Recebe a escolha do usuário
  if r == 1:                                                                                                                      #Chama a função cadastraAluno
    aluno = cadastrarAluno(alunos)
    alunos.append(aluno)
  elif r == 2:                                                                                                                    
    if(len(alunos)>0):  
      nome = input('Digite o nome do aluno: ')
      cadastrarNota(alunos, nome)
    else:
      print('Sem alunos cadastrados')
  elif r == 3:
    if(len(alunos)>0):
      nome = input('Digite o nome do aluno: ')
      consultarAluno(alunos, nome)
    else:
      print('Sem alunos cadastrados')
  elif r == 4:
    if(len(alunos)>0):
      todosOsAlunos(alunos)
    else:
      print('Sem alunos cadastrados')
  elif r == 5:
    if(len(alunos)>0):
      excluirAluno(alunos, nome)
    else:
      print('Sem alunos cadastrados')
  elif r == 0:
    sair()