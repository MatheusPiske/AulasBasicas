#idade = int(input('Digite a sua idade: '))
#Atenção à identação do código.
# O 'if' sempre procura o valor verdadeiro.
#if idade >= 18:
#  print('Você é maior de idade.')
#O 'else' só pode vir imediatamente após o 'if'.
#else:
#  print('Você é menor de idade.')
#ELIF = 'Senão, se'
idade = int(input('Digite a sua idade: '))
if idade >= 18:
  print('Você é maior de idade.')
elif idade == 17:
  print('Você é quase maior de idade.')
else:
  print('Você é menor de idade.')
#!=, não é igual a.
#O Python reconhece qualquer valor vazio ou igual a zero falso:
#if y:
#  print('teste')
#Neste caso, irá dar erro ,uma vez que, 'y' não foi especificado. Neste caso devemos adicionar 'y = 5' por exemplo.