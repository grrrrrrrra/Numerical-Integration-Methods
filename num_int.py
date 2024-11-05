"""
ПРИМЕР РАБОТЫ КОДА:

Введите функцию: 1/(1+x**2)
Введите число отрезков: 10
Нижний предел интегрирования: 0
Верхний предел интегрирования: 1
Нижние прямоугольники: 0.8099814972267897
Верхние прямоугольники: 0.7599814972267898
Трапеции: 0.7849814972267897
Симпсона: 0.7853981534848037
Введите точки через пробел (не больше 6; равноудаленные): 0.0 0.2 0.4 0.6 0.8 1.0
Ньютон-Котес: 0.7854696044815028
"""

def f(fx, x):
  """
  Вычисляет значение заданной строкой функции в зависимости от x

  Args:
      fx (str): Строка / математическое выражение, где 'x' является переменной
      x (float или int): Значение переменной 'x', которое будет подставлено в выражение

  Returns:
      float: Результат вычисления fx с заданным значением x
  """
  return eval(fx)

fx = input('Введите функцию: ')

n = int(input('Введите число отрезков: '))
a = int(input('Нижний предел интегрирования: '))
b = int(input('Верхний предел интегрирования: '))

delta_x = (b - a) / n

# ПРЯМОУГОЛЬНИКИ
summa_niz, summa_verx = 0, 0

for i in range(n):
  xi = i * delta_x + a
  yi = f(fx, xi)
  #print(f'xi = {xi}, yi = {yi}')
  summa_niz += yi

for i in range(1, n + 1):
  xi = i * delta_x + a
  yi = f(fx, xi)
  #print(f'xi = {xi}, yi = {yi}')
  summa_verx += yi

print(f'Нижние прямоугольники: {delta_x * summa_niz}')
print(f'Верхние прямоугольники: {delta_x * summa_verx}')

# ТРАПЕЦИИ
summa_tr = 0

for i in range(n + 1):
  xi = i * delta_x + a
  yi = f(fx, xi)
  #print(f'xi = {xi}, yi = {yi}')
  if i == 0 or i == n:
    summa_tr += yi / 2
  else:
    summa_tr += yi

print(f'Трапеции: {delta_x * summa_tr}')

# СИМПСОН
summa_simpson = 0

for i in range(n + 1):
  xi = i * delta_x + a
  yi = f(fx, xi)
  #print(f'xi = {xi}, yi = {yi}')
  if i == 0 or i == n:
    summa_simpson += yi
  elif i % 2 == 0:
    summa_simpson += 2 * yi
  else:
    summa_simpson += 4 * yi
    
print(f'Симпсона: {delta_x * summa_simpson / 3}')

# НЬЮТОН-КОТЕС
summa_new_cot = 0

def find_c(n, a, b):
  """
    Находит значение коэффициентов в зависимости от числа точек n

  Args:
      n (int): Количество точек
      a (float): Левая граница интервала интегрирования
      b (float): Правая граница интервала интегрирования
  Returns:
      tuple: Коэффициенты для численного интегрирования
  """
  if n == 1:
    c = (b - a) / 2
    return c, c
  elif n == 2:
    c1 = (b - a) / 6
    c2 = 2 * (b - a) / 3
    return c1, c2, c1
  elif n == 3:
    c1 = (b - a) / 8
    c2 = 3 * (b - a) / 8
    return c1, c2, c2, c1
  elif n == 4:
    c1 = 7 * (b - a) / 90
    c2 = 16 * (b - a) / 45
    c3 = 2 * (b - a) / 15
    return c1, c2, c3, c2, c1
  elif n == 5:
    c1 = 19 * (b - a) / 288
    c2 = 25 * (b - a) / 96
    c3 = 25 * (b - a) / 144
    return c1, c2, c3, c3, c2, c1
  elif n == 6:
    c1 = 41 * (b - a) / 840
    c2 = 9 * (b - a) / 35
    c3 = 9 * (b - a) / 280
    c4 = 34 * (b - a) / 105
    return c1, c2, c3, c3, c2, c1
  else:
    print('Слишком большой коэффициент!')
    return None

x = list(map(float, input('Введите точки через пробел (не больше 6; равноудаленные): ').split()))

a = x[0] 
b = x[-1]  

n = len(x) - 1
c = find_c(n, a, b)

for i in range(len(x)):
    summa_new_cot += c[i] * f(fx, x[i])

print(f'Ньютон-Котес: {summa_new_cot}')
