import pandas  # импортирование библиотеки для считывания данных
import matplotlib.pyplot as plt # импорт библиотеки для отрисовки графика 
import numpy as np # импорт библиотеки для реализации вычислений значений


data = pandas.read_csv('ex1data1.csv')
#traffic = pandas.read_tsv('web_traffic.tsv')



count = data["Column1"]
#print(count[0])

x = np.linspace( min(count), max(count),  len(count))
y = (2 * x) - 10


fig = plt.figure()
ax = fig.add_subplot(111)
plt.xticks(np.arange(0, max(count), 1.0))
plt.yticks(np.arange(0, max(y)+2, 2.0))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x, y)
fig.savefig('graph.png')

p = np.polyfit(x,y,1)
f = np.poly1d(p)                
fig1 = plt.figure()
bx  = fig1.add_subplot(111)
bx.plot(x, y)
bx.plot(x,f(x))
fig1.savefig('graph1.png')
