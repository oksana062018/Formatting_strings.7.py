#Использование %
team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %s!" % 5)
print("Итого сегодня в командах участников: %s и %s!" % (5, 6))
#Использование format():
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print("Команда Волшебники данных решила задач: {}!".format(42))
print("Волшебники данных решили задачи за {} с !".format(2153.31451))

#Использование f-строк:
#score_1 = 40
#score_2 = 42
print(f"Команды решили {score_1} и {score_2} задачи.")

#Исход соревнования
challenge_result = ""
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)//2


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья!"

print(challenge_result)

