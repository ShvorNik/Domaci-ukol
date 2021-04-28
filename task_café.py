import random
# ФУНКЦИИ
# количество посетителей за день
def cust():
    customers = random.randrange(5, 21)
    return customers

# количество чашек на посетителя
def cups():
    cups_per_cust = random.randrange(1, 4)
    return cups_per_cust

# преобразатель времени во формат ЧЧ:ММ
def time():
    if times[count] % 60 >= 10:
        time = f'{times[count] // 60 + 9}:{times[count] % 60}'
    else:
        time = f'{times[count] // 60 + 9}:0{times[count] % 60}'
    return time

# время работы кафе в минутах
def max_time():
    max_time = 60 * (20 - 9)
    return max_time

# преобразователь точек пауз во формат ЧЧ:ММ
def br():
    if breaks[b] % 60 >= 10:
        breaks[b] = f'{breaks[b] // 60 + 9}:{breaks[b] % 60}'
    else:
        breaks[b] = f'{breaks[b] // 60 + 9}:0{breaks[b] % 60}'
    return breaks[b]


week = {0: [], 1: [], 2: [], 3: [], 4: []}
results = []
timer = 0
total = [0, 0]
list_of_breaks = {0: [], 1: [], 2: [], 3: [], 4: []}

# цикл для создания рабочей недели
while timer < len(week):
    custo = cust()
    count = 0
    total_cups = 0

# Счётчик-сортировщик
    times = []
    while len(times) < custo:
        number = random.randrange(max_time() + 1)
        for s in times:
            n = times.index(s)
            if times[n] > number:
                times.insert(n, number)
                break
            elif times[n] == number:
                break
        else:
            times.append(number)
    times.insert(0, 0)
    times.append(max_time())

# Определитель пауз больше часа
    breaks = []
    for t in times:
        n = times.index(t)
        if times[n] - times[n - 1] > 60:
            breaks.append(times[n - 1])
            breaks.append(times[n])
    for t in breaks:
        b = breaks.index(t)
        br()
    break_counter = 0
    while break_counter < len(breaks):
        list_of_breaks[timer].append(f'{breaks[break_counter]} - {breaks[break_counter+1]}')
        break_counter += 2

# Обработка результатов за каждый день
    while count < custo:
        count += 1
        cpc = cups()
        total_cups += cpc
        if cpc > 1:
            s = 's'
        else:
            s = ''
        week[timer].append(f'{time()}  {cpc} cup{s}')
    total[0] += total_cups
    total[1] += custo
    results.append(total_cups)
    results.append(custo)
    timer += 1

# Вывод результатов
day = 0
day_of_the_week = ['Mon', 'Tue', 'Wed', 'Tur', 'Fri']
while day < 5:
    print(f'{day_of_the_week[day]}: {week[day]}\n Total: {results[(day)*2]} cups, {results[(day)*2+1]} customers\nBreaks: {list_of_breaks[day]}\n')
    day += 1
print(f'Total for the week: {total[0]} cups, {total[1]} customers')