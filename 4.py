# 4. Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.

# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
#     б). больше 190 см
#     в). от 166 см до 190 см
#     г). от 166 см до 182 см
#     д). от 158 см до 190 см
#     е). не выше 150 см или не ниже 190 см
#     ё). не выше 150 см или не ниже 198 см
#     ж). ниже 166 см.
import math

# параметры распределения
mu = 174
sigma = 8

# функция плотности распределения


def f(x):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - mu)**2 / (2 * sigma**2))

# вероятность больше x


def p_greater(x):
    return 1 - p_less_or_equal(x)

# вероятность меньше или равно x


def p_less_or_equal(x):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

# вероятность от x1 до x2


def p_between(x1, x2):
    return p_less_or_equal(x2) - p_less_or_equal(x1)


# а). больше 182 см
p_a = p_greater(182)
print(
    "Вероятность, что случайный человек имеет рост больше 182 см: {:.2%}".format(p_a))

# б). больше 190 см
p_b = p_greater(190)
print(
    "Вероятность, что случайный человек имеет рост больше 190 см: {:.2%}".format(p_b))

# в). от 166 см до 190 см
p_c = p_between(166, 190)
print(
    "Вероятность, что случайный человек имеет рост от 166 см до 190 см: {:.2%}".format(p_c))

# г). от 166 см до 182 см
p_d = p_between(166, 182)
print(
    "Вероятность, что случайный человек имеет рост от 166 см до 182 см: {:.2%}".format(p_d))

# д). от 158 см до 190 см
p_e = p_between(158, 190)
print(
    "Вероятность, что случайный человек имеет рост от 158 см до 190 см: {:.2%}".format(p_e))

# е). не выше 150 см или не ниже 190 см
p_f = p_less_or_equal(150) + p_greater(190)
print(
    "Вероятность, что случайный человек имеет рост не выше 150 см или не ниже 190 см: {:.2%}".format(p_f))

# ё). не выше 150 см или не ниже 198 см
p_g = p_less_or_equal(150) + p_greater(198)
print(
    "Вероятность, что случайный человек имеет рост не выше 150 см или не ниже 198 см: {:.2%}".format(p_g))

# ж). ниже 166 см
p_h = p_less_or_equal(166)
print(
    "Вероятность, что случайный человек имеет рост ниже 166 см: {:.2%}".format(p_h))
