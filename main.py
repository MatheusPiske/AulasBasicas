from time import sleep
from amoeba import *
print('Vamos calcular o seu IMC?')
sleep(2)

valid_peso = False
while valid_peso == False:
    peso = input('Digite o seu peso: ')
    try:
        peso = float(peso)
        if peso < 0:
          print('Peso inválido.')
        else:
          valid_peso = True
    except:
        print(
            'Formato de peso inválido. Use apenas números e ponto para decimais.'
        )

print('\n')

valid_altura = False
while valid_altura == False:
    altura = input('Digite a sua altura: ')
    try:
        altura = float(altura)
        if altura < 0 or altura > 10:
          print('Altura inválida.')
        else:
          valid_altura = True
    except:
        print(
            'Formato de altura inválido. Use apenas números e ponto para decimais.'
        )

print('\n')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite o seu sexo: ')
    if sexo != 'm' and sexo != 'f':
        print('Esse sexo não consta no sistema. Utilize apenas "M" ou "F".')
    else:
        valid_sexo = True

print('\n')

valor_imc = str(imc(peso, altura))
valor_class = class_imc(sexo, peso, altura)

print('O seu IMC é: ', valor_imc[0:5])
print('A sua classificação é: ', valor_class)
