#1 Первое задание
s = input("Укажите число:")
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

#2 Второе задание
print(input("Укажите число:").count(' ') + 1)

#3 Третье задание
s = input("Укажите число:")
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

#4 Четвертое задание
s = input("Укажите число:")
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))

#5 Пятое задание
s = input("Укажите число:")
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)

#13 Тринадцатое задание
a = int(input("Укажите число:"))
b = int(input("Укажите число:"))
c = int(input("Укажите число:"))
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

#6 Шестое задание
print(input("Укажите число:").replace('1', 'one'))

#7 Седьмое задание
print(input("Укажите число:").replace('@', ''))

#9 Девятое задание
a = int(input("Укажите число:"))
b = int(input("Укажите число:"))
if a < b:
    print(a)
else:
    print(b)

#16 Шестнадцатое задание
n = int(input("Укажите число:"))
m = int(input("Укажите число:"))
x = int(input("Укажите число:"))
y = int(input("Укажите число:"))
# n, m = min(n, m), max(n, m)
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
# print(min(x, y))
if x < y:
    print(x)
else:
    print(y)

#10 Десятое задание
x = int(input("Укажите число:"))
if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)

#11 Одинадцатое задание
x1 = int(input("Укажите число:"))
y1 = int(input("Укажите число:"))
x2 = int(input("Укажите число:"))
y2 = int(input("Укажите число:"))
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

#8 Восмье задание
s = input("Укажите число:")
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)

#12 Двенадцатое задание
year = int(input("Укажите число:"))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')


#14 Четырнадцатое задание
x1 = int(input("Укажите число:"))
y1 = int(input("Укажите число:"))
x2 = int(input("Укажите число:"))
y2 = int(input("Укажите число:"))
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

#15 Пятьнадцатое задание
n = int(input("Укажите число:"))
m = int(input("Укажите число:"))
k = int(input("Укажите число:"))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
