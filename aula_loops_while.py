#'While', estrutura muito parecida com o if;
#Também existe a identação;
#O 'while' procura um verdadeiro ou falso;
#Control C, interompe um loop.
#x = 0
#while x < 1:
#  nome = input('Qual o seu nome? ')
#x = 0
#pessoas = []
#while x < 4:
#  nome = input('Qual é o seu nome? ')
#  pessoas.append(nome)
#  x = x + 1
#  print(pessoas)
#Exemplo do loop para controlar um programa.
#Ao invés de escrever 'x = x + 1', escreva 'x += 1'.
pessoas = []

while 'modalmais' not in pessoas:
  nome = input('Qual é o seu nome? ')
  pessoas.append(nome)
  print(pessoas)
#'Continue' sai do loop e recomeça, 'Break' sai do loop termina
