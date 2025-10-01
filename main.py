from sympy import *
import pandas as pd

k, T, C, L = symbols('k T C L')
# 1 Способ
C_ost = 30000 # молодец Артём
Am_lst = []
C_ost_lst = [] # Что это такое? это создание пустого списка с именем C_ost_lst, C_ost_lst — это будущий столбец "Остаток стоимости" -5
for i in range(8): # молодец Артём 2
  Am = (C - L) / T
  C_ost -= Am.subs({C: 30000, T: 8, L: 0}) # корректно
  Am_lst.append(round(Am.subs({C: 30000, T: 8, L: 0}), 2)) # корректно
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst', Am_lst)
print('C_ost_lst', C_ost_lst) 

#2 способ
Aj = 0
C_ost = 30000 # Что это такое? Инициализируем первоначальную стоимость объекта-5 
Am_lst_2 = []
C_ost_lst_2 = []

for i in range(8):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 30000, T: 8, k: 2})
  Am_lst_2.append(round(Am.subs({C: 30000, T: 8, k: 2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода
import pandas as pd

Y = range(1, 9)

table1 = list(zip(Y, C_ost_lst, Am_lst)) #Зачем эта строка? объединяем три отдельных списка в одну структуру, готовую для создания таблицы, zip соединяет первый элемент из первого списка с первым элементом из второго и третьего списков, второй элемент с вторым и т.д. - получаем список кортежей -5


table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))

tfame = pd.DataFrame(table1, columns=['Y', 'C_cost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_cost_lst_2', 'Am_lst_2'])

print(tfame)
print(tfame2)

# Контейнер визуализации
from matplotlib import pyplot as plt

plt.plot(tfame['Y'], tfame['C_cost_lst'], label='Am')
plt.plot(tfame2['Y'], tfame2['C_cost_lst_2'], label='Am_2')
#plt.show()

vals = Am_lst
labels = list(range(1, 9))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'linewidth': 1, 'edgecolor': 'k'}, rotatelabels=True)
ax.axis('equal')
plt.show()

vals = Am_lst_2
labels = list(range(1, 9))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       shadow=True,
       explode=explode,
       wedgeprops={
           'linewidth': 1,
           'edgecolor': 'k'
       },
       rotatelabels=True)
ax.axis('equal')
plt.show()














# Вариант 2
from sympy import *
import pandas as pd



k, T, C, L = symbols('k T C L')
# 1 Способ
C_ost = 50000
Am_lst = []
C_ost_lst = []
for i in range(9):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 50000, T: 9, L: 0})
    Am_lst.append(round(Am.subs({C: 50000, T: 9, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print('Am_lst', Am_lst)
print('C_ost_lst', C_ost_lst)

#2 способ
Aj = 0
C_ost = 50000
Am_lst_2 = []
C_ost_lst_2 = []

for i in range(9):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 50000, T: 9, k: 2})
    Am_lst_2.append(round(Am.subs({C: 50000, T: 9, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

# Использование pandas
import pandas as pd

Y = range(1, 10)

table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))

tframe = pd.DataFrame(table1, columns=['Y', 'C_cost_lst', 'Am_lst'])
tframe2 = pd.DataFrame(table2, columns=['Y', 'C_cost_lst_2', 'Am_lst_2'])

print(tframe)
print(tframe2)

# Визуализация
from matplotlib import pyplot as plt

#plt.plot(tframe['Y'], tframe['C_cost_lst'], label='Am')
#plt.plot(tframe2['Y'], tframe2['C_cost_lst_2'], label='Am_2')
#plt.show()

vals = Am_lst
labels = list(range(1, 10))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       shadow=True,
       explode=explode,
       wedgeprops={
           'linewidth': 1,
           'edgecolor': 'k'
       },
       rotatelabels=True)
ax.axis('equal')
#plt.show()

vals = Am_lst_2
labels = list(range(1, 10))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       shadow=True,
       explode=explode,
       wedgeprops={
           'linewidth': 1,
           'edgecolor': 'k'
       },
       rotatelabels=True)
ax.axis('equal')
#plt.show()

print('****************')
print("Вывод ключей")

import os

secret = os.environ.get('Lengauer_secret')
print("Свой ключ")
print(secret)
print("Ключ согрупника:")

# Код Артёма Выродова)
import os

print('Код Артёма Выродова:)')
print(os.environ.get('Lengauer_secret'))
print(os.environ.get('Lengauer_secret2'))
print(os.environ.get('Lengauer_secret3'))  # Увидел что поменял

# вот это ты выдал бро
