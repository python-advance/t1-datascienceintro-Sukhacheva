"""
Используя обучающий набор данных о пассажирах Титаника,
находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), визуализируйте данные:
- стоимости билетов пассажиров с помощью диаграммы рассеяния (scatterplot):
по оси X - пассажиры в порядке увеличения PassengerId, по оси Y - стоимость билетов
- проанализировать как наилучшим образом визуализировать данные о ценовом распределении билетов (предложить собственный вариант реализации после создании визуализации ниже).

 Отобразить два графика (subplot) на одном изображении (figure): 
 1. График типа boxplot, на котором отобразить распределение цен билетов по классам (1, 2, 3).
 2. Столбчатую диаграмму (countplot) с распределением средних цен на билеты сгруппированным по трем портам (S, C, Q).

Сохранить получившиеся графики в файлах: result1.png, result2.png.
Настроить название графиков, подписи осей, отобразить риски со числовыми значениями на графике, сделать сетку на графике
(если необходимо для улучшения изучения данных на графике).


"""

import pandas  # импортирование библиотеки для считывания данных
import matplotlib.pyplot as plt  # импорт библиотеки для отрисовки графика
import numpy as np  # импорт библиотеки для реализации вычислений значений

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")

data = pandas.read_csv('train.csv', index_col="PassengerId")



prices = data.sort_values('Fare')
prices = prices["Fare"].value_counts()
##prices = data['Fare']
#prices = prices.sort_values()
count = prices.tolist()
print(count[0])
#prices = prices.keys().sort_values()

#print(len(prices))

x = np.linspace( 0, count[0],  len(count))
y = prices.keys()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xticks(np.arange(0, max(count)+5, 5.0))
plt.yticks(np.arange(0, max(prices.keys()+50), 50.0))
ax.set_xlabel('количество пассажиров купивших  билеты за эту стоимость')
ax.set_ylabel('Стоимость билетов')
ax.scatter(x, y, color = 'black', s = 2)
fig.savefig('graph.png')

