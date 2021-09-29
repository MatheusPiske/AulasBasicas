import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [1000,5300,2000,4500,3000,5000]
legenda = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
plt.xticks(x,legenda)

plt.plot(x,y)
plt.show()


