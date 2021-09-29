import time as t
import matplotlib.pyplot as plt

tempos = []
vezes = []
legenda = []
vez = 1
repet = 4

print(f'Este programa marcará o tempo gasto para digitar a palavra PROGRAMAÇÃO. Você terá que digitá-la {repet} vezes.')
input('Aperte ENTER para começar.')

while vez <= repet:
    inicio = t.perf_counter()
    input('Digite a palavra: ')
    fim = t.perf_counter()
    tempo = round(fim - inicio, 2)
    tempos.append(tempo)
    vezes.append(vez)
    vezstr = str(vez)+'a vez'
    legenda.append(vezstr)
    vez += 1

plt.xticks(vezes, legenda)
plt.plot(vezes, tempos)
plt.show()

input()