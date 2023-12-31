# 1 Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# data = [1,2,3,7,99,0,55,3,5,2,3,0,1,1]
# res = set()
# for i in range(len(data)):
#     if data[i] not in res and data[i] in data[i+1:]:
#         res.add(data[i])
# print(*res)
from itertools import permutations
from math import factorial

# 2 В большой текстовой строке подсчитать количество встречаемыхслов и вернуть 10 самых частых. Не учитывать
# знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
# data_str = 'Business Intelligence\n\
# Материал из Википедии — свободной энциклопедии\n\
# Business intelligence (BI) — обозначение компьютерных методов и инструментов для организаций, обеспечивающих перевод транзакционной деловой информации в человекочитаемую форму, а также средства для массовой работы с такой обработанной информацией.\n\
# \n\
# Цель BI — интерпретировать большое количество данных, заостряя внимание лишь на ключевых факторах эффективности, моделируя исход различных вариантов действий, отслеживая результаты принятия решений.\n\
# \n\
# BI поддерживает множество бизнес-решений — от операционных до стратегических. Основные операционные решения включают в себя позиционирование продукта или цен. Стратегические бизнес-решения включают в себя приоритеты, цели и направления в самом широком смысле. BI наиболее эффективен, когда он объединяет данные, полученные из рынка, на котором работает компания (внешние данные), с данными из источников внутри компании, таких как финансовые и производственные (внутренние данные). В сочетании внешние и внутренние данные дают более полную картину бизнеса, или те самые «структурированные данные» (англ. intelligence) — аналитику, которую нельзя получить только от одного из этих источников.\n\
# \n\
# Термин впервые появился в 1958 году в статье исследователя из IBM Ханса Питера Луна (англ. Hans Peter Luhn), определившего BI как «возможность понимания связей между представленными фактами»[1]. BI в современном понимании эволюционировал из систем для принятия решений, которые появились в начале 1960-х годов и разрабатывались в середине 1980-х годов.\n\
# \n\
# В 1989 году Ховард Дреснер (позже аналитик Gartner) определил Business Intelligence как общий термин, описывающий «концепции и методы для улучшения принятия бизнес-решений с использованием систем на основе бизнес-данных».\n\
# \n\
# Ральф Кимболл выделил три самых важных аспекта для успешной реализации BI-проекта[2]:\n\
# \n\
# уровень финансирования и поддержки со стороны руководства;\n\
# степень востребованности проекта для конкретного бизнеса;\n\
# объём и качество доступных бизнес-данных.\n\
# В 2012 году мировой рынок услуг в сфере Business Intelligence оценивался в $13,1 млрд[3]. По прогнозам специалистов к 2027 году эта сумма будет составлять $60,49 млрд[4].'
#
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~—"""
# for i in punctuation:
#     data_str = data_str.replace(i, '')
# data_str = data_str.replace('\n', ' ').replace('  ',' ').lower()
# data = data_str.split()
# print(data)
# words = {}
# for word in data:
#     if word not in words:
#         words[word] = 1
#     else:
#         words[word] +=1
# print(words)
# words = sorted(words, key = lambda i: words[i], reverse=True)
# print(*words[:10], sep=', ')

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в
# качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
staff = {'sofa': 12, 'torch': 0.1, 'tent': 2.5, 'light': 0.001,\
         'trouthers': 0.2, 'water': 5, 'salami': 2.3, 'topor': 2.7, \
         'sleeping_bag': 3.1, 'alcohol': 4.4, 'buckwheat': 6.1}
capacity = 11
# будем считать, что рюкзак заполнять менее чем на 7кг не прилично
min_wight = 7
# для понимания сколько всего будет размещений
print('размещений', factorial(len(staff)) / factorial(len(staff) - len(staff)))

def wight_of_staff(staff_, razmechenie_, capacity_):
    wight_ = 0
    i = 0
    while wight_ + staff_[razmechenie_[i]] <= capacity_:
        wight_ += staff_[razmechenie_[i]]
        i += 1
    return round(wight_, 2), set(razmechenie_[:i])

sets_of_razm = []
for razmechenie in permutations(staff, 11):
    wight_and_list = wight_of_staff(staff, razmechenie, capacity)
    if wight_and_list[0] >= 7 and wight_and_list[1] not in sets_of_razm:
        sets_of_razm.append(wight_and_list[1])
        print(razmechenie, '->', wight_and_list)
print(len(sets_of_razm))
