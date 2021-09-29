import time
import matplotlib.pyplot as plt
contagem = []

def count_time():
   
    valid_palavra = False
    
    inicio = time.perf_counter()
    palavra1 = input('Digite uma palavra aleatória: ')
    print('\n')
    fim = time.perf_counter()
    tempo = round(fim - inicio, 2)
    contagem.append(tempo)

    inicio2 = time.perf_counter()

    while valid_palavra == False:
        palavra2 = input('Digite essa palavra novamente: ')
        print('\n')
        if palavra1 != palavra2:
            print('Você digitou uma palavra diferente.')
        else:
            valid_palavra = True

    fim2 = time.perf_counter()
    tempo2 = round(fim2 - inicio2, 2)
    contagem.append(tempo2)

    valid_palavra = False
    inicio3 = time.perf_counter()

    while valid_palavra == False:
        palavra3 = input('Digite a mesma palavra novamente: ')
        print('\n')
        if palavra1 != palavra3:
            print('Você digitou uma palavra diferente.')
        else:
            valid_palavra = True

    fim3 = time.perf_counter()
    tempo3 = round(fim3 - inicio3, 2)
    contagem.append(tempo3)

    valid_palavra = False
    inicio4 = time.perf_counter()
    
    while valid_palavra == False:
        palavra4 =  input('Novamente: ')
        print('\n')
        if palavra1 != palavra4:
            print('Você digitou uma palavra diferente.')
        else:
            valid_palavra = True
   
    fim4 = time.perf_counter()
    tempo4 = round(fim4 - inicio4, 2)
    contagem.append(tempo4)

    valid_palavra = False
    inicio5 = time.perf_counter()
    
    while valid_palavra == False:
        palavra5 =  input('Novamente: ')
        print('\n')
        if palavra1 != palavra5:
            print('Você digitou uma palavra diferente.')
        else:
            valid_palavra = True
    
    fim5 = time.perf_counter()
    tempo5 = round(fim5 - inicio5, 2)
    contagem.append(tempo5)

    x = ['1a Vez', '2a Vez', '3a Vez', '4a Vez', '5a Vez']
    y = [tempo, tempo2, tempo3, tempo4, tempo5]
    plt.plot(x, y)
    plt.show()


count_time()
total_contagem = sum(contagem)
print(f"Você demorou {round(total_contagem, 2)} segundos para digitar.")

input()