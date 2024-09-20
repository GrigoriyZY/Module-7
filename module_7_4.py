# Домашнее задание по теме "Форматирование строк"

# Вводные данные
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1+score_2
time_avg = (team1_time + team2_time) / tasks_total
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

# Использование %
print('В команде %s участников %d!' % (team1, team1_num))
print('Итого сегодня в командах %d и %d участников соответственно!' % (team1_num, team2_num))

# Использование format
print('Команда {} решила задач: {}!'.format(team2, score_2))
print('{} решили задачи за {} c.!'.format(team2, team2_time))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы:{result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg: .2f} секунд на задачу!')
