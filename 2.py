# # 2. О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.
a = 0.5
variance = 0.2
b = a + (variance * 12) ** 0.5 * 2
mean = (a + b) / 2

print("Правая граница: ", b)
print("Среднее значение: ", mean)
