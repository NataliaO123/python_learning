print('Здравствуй, мир!')

print(4, 8, 15, 16, 23, 42)

print(4)
print(8)
print(15)
print(16)
print(23)
print(42)

print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')

print('Как тебя зовут?')
name = input()
print('Привет,', name)

# сначала тут печатается строка "Как тебя зовут", а потом принимается на вход имя
name = input('Как тебя зовут?')

# тут просто выводится строка "Привет", после неё идёт пробел и введённое нами имя
print('Привет,', name)

name = input()
print('Привет',name)

name = input()
print(name, '- чемпион!')

x = input()
b1 = input()
a2 = input()

print(a2)
print(b1)
print(x)

print('I', 'like', 'Python', sep='***')

zero = input()
x = input()
b1 = input()
a2 = input()

print(x,b1,a2,sep=zero)

print('Привет,', input(), '!')

x = input()
print(x)
print(int(x)+1)
print(int(x)+2)

x = input()
b1 = input()
a2 = input()
print(int(x)+int(b1)+int(a2))

x = int(input())
V = x*x*x
S = 6*x*x
print('Объем =', V)
print('Площадь полной поверхности =', S)

x = int(input())
b1 = int(input())
x = (x+b1)*(x+b1)*(x+b1)
f = 3*x + 275*b1*b1 - 127*x -41
print(f)

b1 = int(input())
x = b1 - 1
a2 = b1 + 1
print('Следующее за числом', b1, 'число:', a2)
print('Для числа', b1, 'предыдущее число:', x)

x = 'monitor'
x = int(input())
b1 = 'block'
b1 = int(input())
a2 = 'keyboard'
a2 = int(input())
b2 = 'mouse'
b2 = int(input())
s = x + b1 + a2 + b2
bill = s*3
print(bill)

x = int(input())
b1 = int(input())
summa = x + b1
raznosti = x - b1
proizved = x * b1
print(str(x), '+', str(b1), '=', summa)
print(str(x), '-', str(b1), '=', raznosti)
print(str(x), '*', str(b1), '=', proizved)

x = int(input())
b2 = int(input())
n = int(input())
p = x + b2 * (n - 1)
print(p)

x = int(input())
x = 2 * x
b1 = 3 * x
a2 = 4 * x
b2 = 5 * x
print(x, x, b1, a2, b2, sep='---')

x = 82 // 3 ** 2 % 7
print(x)

b1 = int(input())
q = int(input())
n = int(input())
x = b1*q**(n-1)
print(x)

x = int(input())
b1 = x // 100

print(b1)

s = int(input())
m = int(input())
ms = m // s
mb = m % s
print(ms)
print(mb)

x = int(input())
x = x // 2
b1 = x - x
print(b1)

p = int(input())
x = p - 1
b1 = x // 4
a2 = b1 + 1
print (a2)

m = int(input())
h = m // 60
mh = m % 60
print(m, 'мин - это', h, 'час', mh, 'минут.')

x = int(input())
l_d = x % 10
s_d = (x % 100) // 10
f_d = x // 100
b1 = l_d + s_d + f_d
a2 = l_d * s_d * f_d
print('Сумма цифр =', b1)
print('Произведение цифр =', a2)

x = int(input())
a2 = x % 10
b1 = (x % 100) // 10
a1 = x // 100
print(a1, b1, a2, sep='')
print(a1, a2, b1, sep='')
print(b1, a1, a2, sep='')
print(b1, a2, a1, sep='')
print(a2, a1, b1, sep='')
print(a2, b1, a1, sep='')

x = int(input())
b2 = x % 10
a2 = (x % 100) // 10
b1 = (x % 1000) // 100 // 10
a1 = x // 1000
print('Цифра в позиции тысяч равна', a1)
print('Цифра в позиции сотен равна', b1)
print('Цифра в позиции десятков равна', a2)
print('Цифра в позиции единиц равна', b2)

print('Поэма "Мёртвые души" одна из самых интересных')

s = 13
k = -5
b2 = s + 2
s = b2
k = 2 * s
print(s + k + b2)

a1 = 17 // (23 % 7)
b1 = 34 % a1 * 5 - 29 % 4 * 3
print(a1 * b1)

## Прямоугольник с экзамена

print('*' * 17, sep='')
print('*', ' '*15, '*', sep='')
print('*', ' '*15, '*', sep='')
print('*' * 17, sep='')

a1 = int(input())
b1 = int(input())
x = a1**2 + 2*a1*b1 + b1**2
y = (a1 + b1)**2 - 2*a1*b1
print('Квадрат суммы', a1, 'и', b1, 'равен', x)
print('Сумма квадратов', a1, 'и', b1, 'равна', y)

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
x = a1**b1 + a2**b2
print(x)

n = int(input())
a1 = n
b1 = n * 11
a2 = n * 111
s = a1 + b1 + a2
print(s)

a1 = input()
b1 = input()
if a1 == b1:
    print('Пароль принят')
else:
    print('Пароль не принят')

a1 = int(input())
if a1 % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

a1 = int(input())
fourth = a1 % 10
third = (a1 % 100) // 10
second = (a1 % 1000) // 100
first = (a1 % 10000) // 1000
x = first + fourth
y = second - third 
if x == y:
    print('ДА')
else:
    print('НЕТ')

a1 = int(input())
if a1 >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

a1 = int(input())
b1 = int(input())
a2 = int(input())
if a2 - b1 == b1 - a1:
    print('YES')
else:
    print('NO')

a1 = int(input())
b1 = int(input())
if a1 < b1:
    print(a1)
else:
    print(b1)

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 < b1:
    x = a1
else:
    x = b1
if a2 < b2:
    y = a2
else:
    y = b2
if x < y:
    print(x)
else:
    print(y)

a1 = int(input())
if a1 <= 13:
    print('детство')
else:
    if 14 <= a1 <= 24:
        print('молодость')
    else:
        if 25 <= a1 <= 59:
            print('зрелость')
        else:
            print('старость')

a1 = int(input())
b1 = int(input())
a2 = int(input())
s = 0
if a1 >= 0:
    s = a1
if b1 >= 0:
    s = s + b1
if a2 >= 0:
    s = s + a2
if s == 0:
    print(0)
else:
    print(s)

x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

x = int(input())
if 1000 <= x <= 9999 and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')

a1 = int(input())
b1 = int(input())
a2 = int(input())
if a1+b1>a2 and a1+a2>b1 and b1+a2>a1:
    print('YES')
else:
    print('NO')

a1 = int(input())
if (not a1 % 100 == 0 and a1 % 4 == 0) or a1 % 400 == 0:
    print('YES')
else:
    print('NO')

## Ход ладьи

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 == a2 and b1 != b2) or (a1 != a2 and b1 == b2):
    print('YES')
else:
    print('NO')

## Ход короля

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
x = a1 - a2
y = b1 - b2
if (-1 <= (x) <= 1 and -1 <= (y) <= 1) or ((a1 == b1 and a2 == b2) and (-1 <= (x) <= 1 and -1 <= (y) <= 1)):
    print('YES')
else:
    print('NO')

n, k = int(input()), int(input())
if n > k:
    print('NO')
elif n == k:
    print("Don't know")
else:
    print('YES')

a1 = int(input())
b1 = int(input())
a2 = int(input())
if a1 == b1 and b1 == a2:
    print('Равносторонний')
elif (a1 == b1 and b1 != a2) or (a1 != b1 and b1 == a2) or (a1 == a2 and a1 != b1):
    print('Равнобедренный')
else:
    print('Разносторонний')

a1 = int(input())
b1 = int(input())
a2 = int(input())
if b1 < a1 < a2 or a2 < a1 < b1:
    print(a1)
elif a1 < b1 < a2 or a2 < b1 < a1:
    print(b1)
elif a1 < a2 < b1 or b1 < a2 < a1:
    print(a2)

## Количество дней

m = int(input())
if m == 2:
    print(28)
elif m == 4 or 6 or 9 or 11:
    print(30)
else:
    print(31)

w = int(input())
if w < 60:
    print('Легкий вес')
elif 60 <= w < 64:
    print('Первый полусредний вес')
elif 64 <= w < 69:
    print('Полусредний вес')

## Самописный калькулятор

a1 = int(input())
b1 = int(input())
a2 = input()
if a2 == ('+'):
    print(a1+b1)
elif a2 == ('-'):
    print(a1-b1)
elif a2 == ('*'):
    print(a1*b1)
elif a2 == ('/') and b1 != 0:
    print(a1/b1)
elif a2 == ('/') and b1 == 0:
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')

## Цветовой микшер

a1 = input()
b1 = input()
if (a1 == 'красный' and b1 == 'синий') or (a1 == 'синий' and b1 == 'красный'):
    print('фиолетовый')
elif (a1 == 'красный' and b1 == 'желтый') or (a1 == 'желтый' and b1 == 'красный'):
    print('оранжевый')
elif (a1 == 'синий' and b1 == 'желтый') or (a1 == 'желтый' and b1 == 'синий'):
    print('зеленый')
elif a1 == b1 == 'красный':
    print('красный')
elif a1 == b1 == 'желтый':
    print('желтый')
elif a1 == b1 == 'синий':
    print('синий')
else:
    print('ошибка цвета')

a1 = int(input())
if a1 == 0:
    print('зеленый')
elif 1 <= a1 <= 10:
    if a1 % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= a1 <= 18:
    if a1 % 2 != 0:
        print('черный')
    else:
        print('красный')
elif 19 <= a1 <= 28:
    if a1 % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= a1 <= 36:
    if a1 % 2 != 0:
        print('черный')
    else:
        print('красный')
else:
    print('ошибка ввода')

## Пересечение отрезков

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 > a2 and b1 > b2 and b1>a2) or (a1 < a2 and b1 < b2 and b1<a2):
    print('пустое множество')
elif (a1 == a2 and b1 == b2):
    print (a1, b1)
elif a1<=a2<b1<b2:
    print(a2,b1)
    if a2<=a1<b2<b1:
        print(a2,b2)
elif a1<a2<=b2<=b1:
    print(a2,b1)
    if a2<a1<=b1<=b2:
        print(a1,b1)

## Exam 2

year = int(input())
fourth = year % 10
third = (year % 100) // 10
if fourth == 0 and third == 0:
    print('YES')
else:
    print('NO')

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 + b1 + a2 + b2)% 2 == 0:
    print('YES')
else:
    print('NO')

a = int(input())
s = input()
if 10 <= a <= 15 and s == 'f':
    print('YES')
else:
    print('NO')

d = int(input())
if d < 1 or d > 10:
    print('ошибка')
else:
    if d == 1:
        print('I')
    elif d == 2:
        print('II')
    elif d == 3:
        print('III')
    elif d == 4:
        print('IV')
    elif d == 5:
        print('V')
    elif d == 6:
        print('VI')
    elif d == 7:
        print('VII')
    elif d == 8:
        print('VIII')
    elif d == 9:
        print('IX')
    elif d == 10:
        print('X')

n = int(input())
if not (n % 2 == 0):
    print('YES')
else:
    if 2 <= n <= 5:
        print('NO')
    elif 6 <= n <= 20:
        print('YES')
    elif n > 20:
        print('NO')

## Ход слона
## failed
## if a1-a2==b1-b2 or a1-a2==b2-b1:
##    print('YES')
##else:
##  print('NO')
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
sum == a1 + a2 + b1 + b2
if sum % 2 == 0 and (a1 != a2 or b1 != b2):
    print('YES')
else:
    print('NO')

## Ход ферзя

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1-a2==b1-b2 or a1-a2==b2-b1:
   print('YES')
elif (a1 == a2 and b1 != b2) or (b1 == b2 and a1 != a2):
   print('YES')
else:
   print('NO')

a = float(input())
b = float(input())
s = a * b * 0.5
print(s)

## Старушки

s, v1,  v2 = float(input()),  float(input()),  float(input())
v = v1 + v2
t = s / v
print(t)

a = float(input())
if not (a == 0):
    z = a ** (-1)
    print(z)
else:
    print('Обратного числа не существует')
    
f = float(input())
c = 5 * (f - 32) / 9
print(c)

## Dog age

n = float(input())
if n == 1:
    print(10.5)
elif n == 2:
    print(10.5*2)
else:
    print(21 + (n-2) * 4)

a = float(input())
b = a * 10
c = int(b) % 10
print(c)

a = float(input())
b = a % 1
print(b)

a = float(input()) 
b = float(input())
c = float(input())
d = float(input())
e = float(input())
mn = min(a, b, c, d, e)
mx = max(a, b, c, d, e)
print('Наименьшее число =', mn)
print('Наибольшее число =', mx)

## Сортировка трёх

a = float(input()) 
b = float(input())
c = float(input())
first = max(a, b, c)
third = min(a, b, c)
sum = a + b + c
second = sum - first - third
print(first, second, third, sep ='\n')


## Интересное число

a = int(input())
first = a % 10
second = (a // 10) % 10
third = a // 100
mx = max(first, second, third)
mn = min(first, second, third)
s = first + second + third
av = s - mx - mn
if av == mx - mn:
    print('Число интересное')
else:
    print('Число неинтересное')

## Абсолютная сумма

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
s = abs(a) + abs(b) + abs(c) + abs(d) + abs(e)
print(s)

## Манхэттенское расстояние

p1, p2, q1, q2 = int(input())
mr = abs(p1 - q1) + abs(p2 - q2)
print(mr)

mystr = 'да'
mystr = mystr + 'нет'
mystr = mystr + 'да'
print(mystr)

str1 = '1'
str2 = str1 + '2' + str1
str3 = str2 + '3' + str2
str4 = str3 + '4' + str3
print(str4)

mystr = '123' * 3 + '456' * 2 + '789' * 1
print(mystr)

s1 = '\"Python is a great language!\"'
s2 = ', said Fred.'
s3 = ' \"I don\'t ever remember having this much fun before.\"'
print(s1 + s2 + s3)

n = input()
f = input()
print('Hello', n, f, '!', 'You have just delved into Python')

f = input()
l = len(f)
print('Футбольная команда', f, 'имеет длину', l, 'символов')

c1 = input()
c2 = input()
c3 = input()
lc1 = len(c1)
lc2 = len(c2)
lc3 = len(c3)
max_l = max(lc1, lc2, lc3) 
min_l = min(lc1, lc2, lc3)
if max_l == lc1:
    print(c1)
elif max_l == lc2:
    print(c2)
else:
    print(c3)
if min_l == lc1:
    print(c1)
elif min_l == lc2:
    print(c2)
else:
    print(c3)

s1 = input()
s2 = input()
s3 = input()
l1 = len(s1)
l2 = len(s2)
l3 = len(s3)
max_l = max(l1, l2, l3)
min_l = min(l1, l2, l3)
av = (l1 + l2 + l3) - max_l - min_l
x = max_l - av
y = av - min_l
if x == y:
    print('YES')
else:
    print('NO')

s = input()
sub_s = 'синий'
if sub_s in s:
    print('YES')
else:
    print('NO')

s = input()
sub_s1 = 'суббота'
sub_s2 = 'воскресенье'
if sub_s1 in s or sub_s2 in s:
    print('YES')
else:
    print('NO')

email = input()
val1 = '@'
val2 = '.'
if val1 in email and val2 in email:
    print('YES')
else:
    print('NO')

## Запуск команды из модуля math

import math
print(math.sqrt(2))

from math import *
print(math.sqrt(2))

from math import *
a = float(input())
b = float(input())
c = float(input())
d = float(input())
l = sqrt((a-c)**2 + (b-d)**2)
print(l)

from math import *
r = float(input())
s = pi*r**2
c = 2*pi*r
print(s)
print(c)

from math import *
a = float(input())
b = float(input())
k = (a+b)/2
l = sqrt(a*b)
m = 2*a*b/(a+b)
n = sqrt((a*a+b*b)/2)
print(k)
print(l)
print(m)
print(n)
 
from math import *
x1 = float(input())
x = x1*pi/180
y = sin(x) + cos(x) + tan(x)**2
print(y)

from math import *
x = float(input())
x1 = ceil(x)
x2 = floor(x)
print(x1+x2)

## Квадратное уравнение

from math import *
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
    if x1 < x2:
        print (x1, x2, sep='\n')
    else:
        print(x2, x1, sep='\n')
elif d == 0:
    x = (-b/(2*a))
    print(x)
elif d < 0:
    print('Нет корней')

from math import *
a = float(input())
n = float(input())
s = (n*a**2)/(4*tan(pi/n))
print(s)

for i in range(10):
    print('Python is awesome!')

s = input()
c = int(input())
for _ in range(c):
    print(s)

for x in range(6):
    print('AAA')
for y in range(5):
    print('BBBB')
print('E')
for z in range(9):
    print('TTTTT')
print('G')

h = int(input())
for x in range(h):
    print('*'*19)

a = input()
for i in range(10):
    print(i, a)

n = int(input())
for i in range(n+1):
    print('Квадрат числа', i, 'равен', i**2)

## Звездный треугольник

n = int(input())
for i in range(n-1):
    print('*'*(i-1))

## Популяция

m = float(input())
p = float(input())
n = float(input())
for i in range(n):
    if i == 0:
        print(1, m)
    else:
        a = m * (1 + (p/100))**(n - 1)
        print(i + 1, a)

m = int(input())
n = int(input())
a = 1 + n
for i in range(m, a):
    print(i)

m = int(input())
n = int(input())
a = 1 + n
if m < n:
    for i in range(m, a):
        print(i)
else:
    for i in range(m, a):
        print(i - m)

m = int(input())
n = int(input())
for i in range (m, n +1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)

## Таблица умножения

n = int(input())
for i in range (1, 11):
    print(n, 'x', i, '=', n*i)

total = 0
for i in range(1, 101):
    total = total + i
print('Сумма равна', total)

total = 0
for i in range(1, 6):
    total += i
    print(total, end="")

a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if (i**3 % 10) == 4 or (i**3 % 10) == 9:
        count += 1
print(count)

n = int(input())
count = 0
for i in range(n, n+1):
    count = count + 1

p = 1
for i in range(11):
    a = int(input())
    if a != 0:
        p = p * a
print(a)

n = int(input())
s = 0
for i in range(1, n + 1):
    if n % i == 0:
        s = s +  i
print(s)

## Асимптотическое приближение

import math
n = int(input())
count = 0
if n != 0:
    for i in range(1, n+1):
        count = (count + 1/i)
a = count - math.log(n)
print(a)

## Знакочередующаяся сумма

n = int(input())
count = 0
for i in range(n):
    if i % 2 == 0:
        count += i + 1
    else:
        count -= i + 1
print(count)

n = int(input())
mx = 0
mx2 = 0
for i in range(n):
    m = int(input())
    if m > mx:
        mx2 = mx
        mx = m
    if m > mx2 and m != mx:
        mx2 = m
print(mx)       
print(mx2)

## Only even numbers

count1 = 0
count2 = 0
for i in range(10):
    m = int(input())
    if m % 2 == 0:
        count1 += m
    else:
        count2 +=m
if count2 != 0:
    print('NO')
else:
    print('YES')

## Последовательность Фибоначчи

n = int(input())
F1 = 0
F2 = 1
for i in range(0, n):
    F1,F2 = F2,F1 + F2
    print(F1, end=' ')

## Till the END

a = input()
while a != 'КОНЕЦ':
    print(a)
    a = input()

## Till the END 2

a = input()
count = 0
while a != 'стоп' and a != 'хватит' and a != 'достаточно':
    count += 1
    a = input()
print(count)

a = int(input())
while a % 7 == 0:
    print(a)
    a = int(input())

## Сумма неотрицательных чисел

a = 0
s = 0
while a >= 0:
    s += a
    a = int(input())
print(s)

## Количество пятерок

a = 1
count = 0
while 0 < a <= 5:
    a = int(input())
    if a == 5:
        count += 1
print(count)

## Ведьмаку заплатите чеканной монетой

n = int(input())
count = 0
while n >= 25:
    count += 1
    n = n - 25
while 10 <= n < 25:
    count += 1
    n = n - 10
while 5 <= n < 10:
    count += 1
    n = n - 5
while 1 <= n < 5:
    count += 1
    n = n - 1
print (count)
    
## Обратный порядок

n = int(input())
while n != 0:
    last_d = n % 10
    n = n // 10
    print(last_d)

## Обратный порядок 2
    
n = int(input())
while n != 0:
    last_d = n % 10
    n = n // 10
    print(last_d, end = '')

## max and min
    
n = int(input())
mx = 0
mn = 9

while n != 0:
    last_d = n % 10
    if last_d < mn:
        mn = last_d
    if last_d > mx:
            mx = last_d
    n = n // 10
print('Максимальная цифра равна', mx)
print('Минимальная цифра равна',mn)

## Все вместе

n = int(input())
last_d = n % 10
amount = 0
s = 0
p = 1
while n != 0:
    l_d = n % 10
    amount += 1
    s += l_d
    p *= l_d
    n = n // 10
first_d = l_d
s_a = s / amount
print(s)
print(amount)
print(p)
print(s_a)
print(first_d)
print(first_d + last_d)

## Вторая цифра

n = int(input())
m = n
while n != 0:
    current_d = n % 10
    n = n // 10
first_d = current_d
while m != first_d:
    new_current_d = m % 10
    m = m // 10
second_d = new_current_d
print(second_d)

n = int(input())
last_d = n % 10
count = 0
while n != 0:
    current_d = n % 10
    if current_d != last_d:
        count += 1
    n = n // 10
if count != 0:
    print('NO')
else:
    print('YES')

## Упорядоченные цифры

n = int(input())
m = 0
amount = 0
counter = 0
while n != 0:
    cur_d = n % 10
    amount += 1
    if cur_d >= m:
        m = cur_d
        counter += 1
    n = n // 10
print(amount)
print(counter)
if counter == amount:
    print('YES')
else:
    print('NO')

mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)

n = int(input())
for i in range(1, n + 1):
    if n % i == 0 and i != 1:
        print(i)
        break

n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    else:
        print(i)

text = input()
count_pair = 0
for i in range(0, len(text) - 1):
    if text[i] == text[i+1]:
        count_pair += 1
print(count_pair)

n = input()
s_plus = 0
s_mult = 0
for i in range(len(n)):
    if n[i] in '+':
        s_plus += 1
    elif n[i] in '*':
        s_mult += 1
print('Символ', '+', 'встречается', s_plus, 'раз')
print('Символ', '*', 'встречается', s_mult, 'раз')

text = input()
s = 0
for i in range(len(text)):
    if text[i] in '0123456789':
        s += int(text[i])
if s > 0:
    print('Цифра')
else:
    print('Цифр нет')

text = input()
for i in range(1, len(text) + 1):
    print(text[-i])

## Decimal to Binary

n = int(input())
a = n
binary_l = ''
while a > 0:
    binary_d = str(a % 2)
    binary_l = binary_d + binary_l
    a //= 2
print(binary_l)

## Палиндром

text = input()
rev = text[::-1]
if rev == text:
    print('YES')
else:
    print('NO')

## Срезы 1

stroka = input()
dlina = len(stroka)
print(dlina)
povtor = stroka*3
print(povtor)
a = stroka[0]
print(a)
aaa = stroka[0:3]
print(aaa)
zzz = stroka[(len(stroka) - 3):]
print(zzz)
rev = stroka[::-1]
print(rev)
udal = stroka[1:(len(stroka)-1)]
print(udal)

## Срезы 2

stroka = input()
print(stroka[2])
print(stroka[len(stroka)-2])
print(stroka[:5])
print(stroka[:(len(stroka)-2)])
a = ''
b = ''
for i in range(len(stroka)):
    if i % 2 == 0:
        a += stroka[i]
    else:
        b += stroka[i]
print(a)
print(b)
rev = stroka[::-1]
print(rev)
rev2 = stroka[len(stroka)::-2]
print(rev2)

## Две половинки

import math
stroka = input()
if len(stroka) % 2 == 0:
    a = round(int(len(stroka)/2))
else:
    a = math.ceil(float(len(stroka)/2))
part1 = stroka[:a]
part2 = stroka[a:]
print(part2, part1, sep='')

## Заглавные буквы

n_f = input()
if n_f == n_f.title():
    print('YES')
else:
    print('NO')

str_a = input()
str_b = str_a.swapcase()
print(str_b)

stroka = input()
stroka_1 = stroka.lower()
str = 'хорош'
if str in stroka_1:
    print('YES')
else:
    print('NO')

## Количество буквенных символов в нижнем регистре

stroka = input()
count = 0
for i in range(len(stroka)):
    if stroka[i] in 'abcdefghijklmnopqrstuvwxyz':
        count += 1
print(count)

## Количество слов

stroka = input()
count = stroka.count(' ')
print(count + 1)

## Минутка генетики

g = input()
gen = g.lower()
a = 0
c = 0
t = 0
g = 0
for i in range(len(gen)):
    if gen[i] in 'а':
        a += 1
    elif gen[i] in 'ц':
        c += 1
    elif gen[i] in 'т':
        t += 1
    elif gen[i] in 'г':
        g += 1
print('Аденин:', a)
print('Гуанин:', g)
print('Цитозин:', c)
print('Тимин:', t)

gen = input().upper()
a = gen.count('А')
g = gen.count('Г')
c = gen.count('Ц')
t = gen.count('Т')
print("Аденин:",  a)
print("Гуанин:", g)
print("Цитозин:", c)
print("Тимин:", t)

## Очень странные дела

n = int(input())
count = 0
for i in range(n):
    sms = input()
    if sms.count('11') >= 3:
        count += 1
print(count)      

## 1
stroka = input()
count = 0
for i in range(len(stroka)):
    if stroka[i] in '0987654321':
        count += 1
print(count)

## 2
text = input()
count = 0
for i in range(10):
    count += text.count(str(i))
print(count)

## .com or .ru

stroka = input()
flag = False
if stroka.endswith('.ru') or stroka.endswith('.com'):
    flag = True
if flag == True:
    print('YES')
else:
    print('NO')

## Самый частотный символ
    
s = input()
max_count = 0
max_char = ''
for i in s:
    if s.count(i) >= max_count:
        max_count = s.count(i)
        max_char = i
print(max_char)

## Первое и последнее вхождение

s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')

## Удаление фрагмента

s = input()
first_h = s.find('h')
last_h = s.rfind('h')
if first_h != -1 and last_h != -1:
    print(s[:first_h], s[last_h+1:], sep='')
else:
    print(s)

## Символы в диапазоне

a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(chr(i), end = ' ')

## Простой шифр
    
lane = input()
for i in lane:
    print(ord(i), end = ' ')

## Шифр Цезаря

n = int(input())
text = input()
decoded_text = ''
for char in text:
    decoded_char = chr(ord(char) - n)
    if decoded_char < 'a':
        decoded_char = chr(ord(char) - n + 26)
    decoded_text += decoded_char
print(decoded_text)

## Каждый третий

l = input()
l1 = ''
for i in range(len(l)):
    if i % 3 != 0:
        l1 = l1 + l[i]
print(l1)

## Замени меня полностью

l = input()
print(l.replace('1', 'one'))

## Удали меня полностью

l = input()
print(l.replace('@', ''))

## Второе вхождение

l = input()
count = 0
for i in range(len(l)):
    if l[i] == 'f':
        count += 1
if count == 0:
    print('-2')
elif count == 1:
    print('-1')
else:
    new_l = l.replace('f', '')
    print(new_l.find('f'))

## Переворот
    
l = input()
a = l.find('h')
b = l.rfind('h')
sub_l1 = l[a:b+1]
sub_l2 = sub_l1[::-1]
print(l[:a] + sub_l2 + l[b+1:])

## Список

n = int(input())
num = list(range(1, n+1))
print(num)

## Список букв

n = int(input())
alf = []
for i in range(n):
    l = chr(ord('a') + i)
    alf += l
print(alf)

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

## Список строк

n = int(input())
s = []
for i in range(n):
    l = input()
    s.append(l)
print(s)

## Алфавит

s = []
for i in range(26):
    s.append(chr(ord('a')+i)*(i+1))
print(s)

## Список кубов

n = int(input())
l = []
for i in range(n):
    m = int(input())
    l.append(m**3)
print(l)

## Список делителей

n = int(input())
l = []
for i in range(1, n + 1):
    if n % i == 0:
        l.append(i)
print(l)

## Суммы двух

n = int(input())
l1 = []
l2 = []
for i in range(n):
    m = int(input())
    l1.append(m)
for i in range(len(l1)-1):
    l2.append(l1[i]+l1[i+1])
print(l2)

n = int(input())
l = []
for i in range(n):
    m = int(input())
    l.append(m)
del l[1::2]
print(l)

## k-ая буква слова

n = int(input())
l = []
for _ in range(n):
    m = input()
    l.append(m)
k = int(input())
result = ''
for i in l:
    if len(i) >= k:
        result += i[k-1]
print(result)

## Символы всех строк

n = int(input())
l = []
for _ in range(n):
    m = input()
    l += m
print(l)

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
s = 0
for num in numbers:
    n = num**2
    s += n
print(s)

## Значение функции

n = int(input())
l1 = []
for _ in range(n):
    m = int(input())
    print(m)
    f = m**2 + 2*m + 1
    l1.append(f)
print()
print(*l1)

## Remove outliers

n = int(input())
l1 = []
for _ in range(n):
    m = int(input())
    l1.append(m)
l1.remove(max(l1))
l1.remove(min(l1))
print(*l1, sep = '\n')

## Без дубликатов

n = int(input())
l = []
for _ in range(n):
    m = input()
    l.append(m)
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(*l1, sep = '\n')

## Google search - 1

n = int(input())
base = []
for _ in range(n):
    data = input()
    base.append(data)
request = input()
for i in base:
    if request.lower() in i.lower():
        print(i)

## Google search - 2

n = int(input())
base = []
for _ in range(n):
    data = input()
    base.append(data)
k = int(input())
requests = []
for _ in range(k):
    request = input().lower()
    requests.append(request)
temp = []
count = 0
for i in base:
    count = 0
    for j in requests:
        if j in i.lower():
            count += 1
            if count == len(requests):
                temp.append(i)
print(*temp, n = '\n')


## Negatives, Zeros and Positives

n = int(input())
l1 = []
l2 = []
l3 = []
temp = []
for _ in range(n):
    m = int(input())
    if m < 0:
        l1.append(m)
    if m == 0:
        l2.append(m)
    if m > 0:
        l3.append(m)
print(*l1, sep = '\n')
print(*l2, sep = '\n')
print(*l3, sep = '\n')

n = input()
new_n = n.split()
print(*new_n, sep = '\n')

## Инициалы

ifo = input()
initials = ifo.split()
lane_i = initials[0]
print(lane_i)
i = lane_i[0]
print(i)
lane_f = initials[1]
print(lane_f)
f = lane_f[0]
print(f)
lane_o = initials[2]
print(lane_o)
o = lane_o[0]
print(o)
print(i, f, o, sep = '.', end = '.')
## Better solution:
ifo = input().split()
print(ifo[0][0], ifo[1][0], ifo[2][0], sep = '.', end = '.')

## Windows OS

path = input()
l = path.split('\\')
print(*l, sep = '\n')

## Диаграмма

stroka = input().split()
for i in range(len(stroka)):
    stroka[i] = int(stroka[i])
    print('+' * stroka[i])

## IP address
    
address = input().split('.')
count = 0
for i in range(len(address)):
    address[i] = int(address[i])
    if 0 <= address[i] <= 255:
        count += 1
if count == 4:
    print('ДА')
else:
    print('НЕТ')
## optimised version
address = input().split('.')
for i in address:
    if int(i) < 0 or int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')

## Добавь разделитель

lane = input()
separator = input()
print(separator.join(lane))

## Количество совпадающих пар

lane = input().split()
count = 0
for i in range(len(lane)):
    lane[i] = int(lane[i])
for i in range(len(lane)):
    for j in range(i + 1, len(lane)):
        if lane[i] == lane[j]:
            count += 1
print(count)

## Все сразу 2

#v1
numbers = [8, 9, 10, 11]
#v2
numbers = [8, 9, 10, 11]
numbers.remove(numbers[1])
numbers.insert(1, 17)
numbers.extend([4, 5, 6])
del numbers[0]
numbers_copy = numbers.copy() + numbers
numbers_copy.insert(3, 25)
print(numbers_copy)

## min-><-max

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
mx = max(numbers)
mx_i = numbers.index(mx)
lane_mx = numbers.pop(mx_i)
mn = min(numbers)
mn_i = numbers.index(mn)
lane_mn = numbers.pop(mn_i)
numbers.insert(mn_i, mx)
numbers.insert(mx_i, mn)
print(*numbers)
## better solution:
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
mx_i = numbers.index(max(numbers))
mn_i = numbers.index(min(numbers))
numbers[mx_i], numbers[mn_i] = numbers[mn_i], numbers[mx_i]
print(*numbers)

story = input().lower().split()
cnt2 = story.count('a')
cnt4 = story.count('an')
cnt6 = story.count('the')
print('Общее количество артиклей:', cnt2 + cnt4 + cnt6)

## Сортировка чисел

s = input()
n = s.split()
for i in range(len(n)):
    n[i] = int(n[i])
n.sort()
print(*n)
n.sort(reverse=True)
print(*n)

## Списочные выражения
#v2
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i[1:] for i in keywords]

print(new_keywords)

## Palindromes

palindromes = [i for i in range(100, 1001) if i % 10 == i // 10]
print(palindromes)
## or:
palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
print(palindromes)

n = int(input())
l = [i**2 for i in range(1, n + 1)]
print(*l, sep = '\n')
#for i in l:
#   print(i)

s = input().split()
l = [int(s[i])**3 for i in range(len(s))]
for i in l:
    print(i, end = ' ')

text = input().split()
print(*text, sep = '\n')
#print (*input().split(),sep='\n')

text = input()
l = ''
for i in text:
    if i in '0987654321':
        l += i
print(l)

#digits = [i for i in input() if i.isdigit()]
#print(*digits, sep="")

text = input().split()
print(text)
l = []
for i in range(len(text)):
    text[i] = int(text[i])
    if text[i] % 2 == 0:
        if text[i]**2 % 10 != 4:
            l.append(text[i]**2)
print(l)

## Список четных

n = [i for i in range(2, int(input()) + 1, 2)]
print(n)

L = input().split()
M = input().split()
for i in range(len(L)):
    L[i] = int(L[i])
for i in range(len(M)):
    M[i] = int(M[i])
LM = []
for i in range(len(L)):
    LM.append(L[i] + M[i])
print(*LM)
#better solution:
L = input().split()
M = input().split()
n = len(L)
l = [int(L[i]) + int(M[i]) for i in range(n)]
print(*l)

l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
s = sum(l)
print(*l, sep='+',end='=')
print(s)

## The longest

line = input().split()
l = 0
for i in range(len(line)):
    if len(line[i]) > l:
        l = len(line[i])
print(l)
#one-lane-solution:
line = [len(i) for i in input().split()]
print(max(line))

## Translater-transformer

words = [word[1:] + word[0] + "ки" for word in input().split()]
print(*words)

## Validation

phone = input().split('-')
lens = [len(part) for part in phone]

if lens == [1, 3, 3, 4] and ''.join(phone).isdigit():
    print('YES')
elif lens == [3, 3, 4] and ''.join(phone).isdigit():
    print('YES')
else:
    print('NO')

## Звездный прямоугольник 1

def draw_box():
    for i in range(14):
        if i in (0, 13):
            print ('*' * 10)
        else:
            print('*', ' ' * 8, '*', sep = '')

draw_box()

## Звездный треугольник 1

def draw_triangle():
    for i in range(1, 11):
        print('*' * i)

draw_triangle()

## Звездный треугольник

def draw_triangle(fill, base):
    temp_base = (base // 2) + 2
    for i in range(1, temp_base):
        print('*' * i)
    for j in range(base // 2, 0, -1):
        print('*' * j)

fill = input()
base = int(input())
draw_triangle(fill, base)

## Initials

def print_fio(name, surname, patronymic):
    print(surname[0] + name[0] + patronymic[0])

name, surname, patronymic = input().capitalize(), input().capitalize(), input().capitalize()

print_fio(name, surname, patronymic)

## Сумма цифр

def print_digit_sum(num):
    d = 0
    while num > 0:
        d += num % 10
        num //= 10
    print(d)
    
n = int(input())
print_digit_sum(n)

## km to miles

def convert_to_miles(km):
    miles = km * 0.6214
    return miles

num = int(input())

print(convert_to_miles(num))

## days in month

def get_days(month):
    if month == 2:
        result = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        result = 30
    else:
        result = 31
    return(result)

num = int(input())

print(get_days(num))

## Делители 1

def get_factors(num):
    l = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            l.append(i)
    l.append(num)
    return(l)

n = int(input())
print(get_factors(n))

## Делители 2

def number_of_factors(num):
    l = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            l.append(i)
    l.append(num)
    return(len(l))
n = int(input())
print(number_of_factors(n))

## Find all

def find_all(target, symbol):
    l = []
    if symbol in target:
        for i in range(len(target)):
            if target[i] == symbol:
                l.append(i)
    else:
        l = []
    return(l)

s = input()
char = input()

print(find_all(s, char))

## Merge lists 1

def merge(list1, list2):
    result = list1 + list2
    result.sort()
    return(result)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))

## Merge lists 2

def quick_merge(list1, list2):
    sorted_list = []
    temp1 = 0
    temp2 = 0
    while temp1 < len(list1) and temp2 < len(list2):
        if list1[temp1] <= list2[temp2]:
            sorted_list.append(list1[temp1])
            temp1 += 1
        else:
            sorted_list.append(list2[temp2])
            temp2 += 1
    if temp1 < len(list1):
        sorted_list += list1[temp1:]
    else:
        sorted_list += list2[temp2:]
    return(sorted_list)

l1 = []
for i in range(int(input())):
    l2 = [int(i) for i in input().split()]
    l1 = quick_merge(l1, l2)     
    
print(*l1)

## Is Valid Triangle?

def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())

print(is_valid_triangle(a, b, c))

## Is a Number Prime?

def is_prime(num):
    count = 0
    if num == 1:
        return False
    else:
        for i in range(1, num + 1):
            if num % i == 0:
                count +=1
        if count > 2:
            return False          
    return True
n = int(input())
print(is_prime(n))
# faster version of is_prime:
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

## Next Prime

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    result = num + 1
    while not is_prime(result):
        result += 1
    return(result)
n = int(input())
print(get_next_prime(n))

## Good password

def is_password_good(password):
    count = 0
    if len(password) >= 8:
        count += 1
        if password.isalnum():
            count += 1
            if password.islower() or password.isupper():
                count -= 1
            if password.isalpha() or password.isdigit():
                count -= 1
    
    if count == 2:
        return True
    else:
        return False

txt = input()
print(is_password_good(txt))

## Ровно в одном

def is_one_away(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    if len(word1) - count == 1:
        return True
    else:
        return False

txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))

## Палиндром

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False

txt = input()
print(is_palindrome(txt))

## BEEGEEK

def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False

def is_prime(num):
    n = int(num)
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_even(num):
    n = int(num)
    if n % 2 == 0:
        return True
    else:
        return False
    
def is_valid_password(password):
    for i in range(len(password)):
        if password[i] in '1234567890:':
            p = password.split(':')
            if len(p) == 3:
                a = p[0]
                b = p[1]
                c = p[2]
                if is_palindrome(a) and is_prime(b) and is_even(c):
                    return True
        else:
            return False
    else:
        return False

psw = input()
print(is_valid_password(psw))
