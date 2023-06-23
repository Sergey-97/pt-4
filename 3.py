# 3. Непрерывная случайная величина X распределена нормально и задана плотностью распределения f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)

# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)
import math
# параметры распределения
mu = -2
sigma = math.sqrt(32)
# функция плотности распределения


def f(x):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - mu)**2 / (2 * sigma**2))
# математическое ожидание


def expected_value():
    return mu
# дисперсия


def variance():
    return sigma**2
# среднее квадратичное отклонение


def standard_deviation():
    return sigma


print("Математическое ожидание: ", expected_value())
print("Дисперсия: ", variance())
print("Среднее квадратичное отклонение: ", standard_deviation())
