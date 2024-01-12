'''1. Сколько секунд в 42 минутах и 42 секундах?'''
minute: int = 42
seconds: int = 42
time: int = minute * 60 + seconds
print(time)

'''2. Сколько миль в 10 километрах? Подсказка: одна миля равна 1,61 км.'''
km: int = 10
mile: float = km * 1.61
print(mile)

'''3. Если вы пробежали 10 километров за 42 минуты 42 секунды, каков
ваш средний темп бега (время, затраченное на преодоление мили,
в минутах и секундах)? Какова ваша средняя скорость в милях в час?'''
#1
road_km: int = 10
time_hours: float = 42.42
mile: float = road_km * 1.61
avg_running_pace: float = 42.42 / mile * 60
print(avg_running_pace)
#2
avg_running_pace_hour: float = 42.42 / mile
print(avg_running_pace_hour)