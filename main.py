perguntas = {
  'Pergunta 1':{
    'pergunta':'quanto é 2 + 2?',
    'respostas':{
      'a': '1',
      'b': '4',
      'c': '7'
    },
    'resposta_certa':'b',
  },
  'Pergunta 2':{
    'pergunta':'quanto é 5 + 5?',
    'respostas':{
      'a': '10',
      'b': '5',
      'c': '7'
    },
    'resposta_certa':'a',
  },
  'Pergunta 3':{
    'pergunta':'quanto é 50 * 1?',
    'respostas':{
      'a': '51',
      'b': '5',
      'c': '50'
    },
    'resposta_certa':'c',
  },
}

respostas_certas = 0

for chave_pergunta, valor_pergunta in perguntas.items():
  print(f'{chave_pergunta} : {valor_pergunta["pergunta"]}')

  print('')
  print('Respostas: ')
  for chave_resposta, valor_resposta in valor_pergunta["respostas"].items():
    print(f'[{chave_resposta}] : {valor_resposta}')

  resposta_usuario = input('Sua resposta: ')

  if resposta_usuario.lower() == valor_pergunta['resposta_certa']:
    respostas_certas += 1
    print()
    print('Você acertou! ')
  else:
    print()
    print('Você errou !')


quantidade_perguntas = len(perguntas)

porcentagem_acertos = respostas_certas / quantidade_perguntas * 100


print()
print('QUIZ FINALIZADO!')
print(f'Total de acertos: {respostas_certas}')
print(f'Porcentagem de acertos: {porcentagem_acertos:.1f}%')
    
    