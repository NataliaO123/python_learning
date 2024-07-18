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

## Ave Caesar

#
l = input().split()
coded_l = []
for word in l:
    coded_word = ''
    for char in word:
        if char.isalpha():
            coded_char = chr(ord(char) - len(word))
            if coded_char < 'a':
                coded_char = chr(ord(char) - len(word) + 26)
            coded_word += coded_char
        else:
            coded_word += char
    coded_l.append(coded_word)
#
l = input().split()
coded_l = []
for word in l:
    coded_word = ''
    count_len = 0
    for char in word:
        if char.isalpha():
            count_len += 1
            coded_char = chr(ord(char) - count_len)
            if coded_char < 'a':
                coded_char = chr(ord(char) - count_len + 26)
            coded_word += coded_char
        else:
            coded_word += char
    coded_l.append(coded_word)
##
def caesar(word, shift):
    encr_word = ''
    for char in word:
        if char.isalpha():
            if char.islower():
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            shifted_char = char
        encr_word += shifted_char
    return encr_word

l = input().split()
new_l = []
for word in l:
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    new_word = caesar(word, count)
    new_l.append(new_word)
print(*new_l)

## Угадайка слов - Hangman

import random as r
word_list = ['камень', 'ножницы', 'бумага', 'ящерица', 'вулканец', 'капитан', 'энтерпрайз', 'планета']

def get_word():
    result = r.choice(word_list).upper()
    return result

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)
    guessed_letters = [] 
    guessed_words = []
    tries = 6 
    guessed = False  
    print("Let's play!")
    print(display_hangman(6))
    print(word_completion)
    while guessed == False:
        for i in range(1, 6):
            print('Введи букву...')
            g_letter = input().upper()
            guessed_letters.append(g_letter)
            if g_letter in word:
                
        


    



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

## Правильная скобочная последовательность

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return len(text) == 0

txt = input()
print(is_correct_bracket(txt))

## snake_case

def convert_to_python_case(text):
    t = text[0].lower()
    for i in range(1, len(text) + 1):
        if text[i].isupper():
            t += '_' + text[i].lower()
        else:
            t += text[i]
    return t

txt = input()
print(convert_to_python_case(txt))

## Middle

def get_middle_point(x1, y1, x2, y2):
    m_x = (x1 + x2) / 2
    m_y = (y1 + y2) / 2
    return(m_x, m_y)

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())
print(x, y)

## Circle

from math import pi

def get_circle(radius):
    c = 2 *pi * radius
    s = pi * radius ** 2
    return c, s
	
r = float(input())
length, square = get_circle(r)
print(length, square)

## Корни уравнения

def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = x2 = -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
    return min(x1, x2), max(x1, x2)
a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)

## Калькулятор доставки

def get_shipping_cost(quantity):
    s = 1000 + (quantity - 1) * 120
    return s

n = int(input())
print(get_shipping_cost(n))

## Искомый месяц

def get_month(language, number):
    m_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    m_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return m_ru[number - 1]
    else:
        return m_en[number - 1]

lan = input()
num = int(input())
print(get_month(lan, num))

## Магические даты

def is_magic(date):
    d = [int(i) for i in date.split('.')]

    num = d[2]
    digit = 0
    m_digit = ''

    while num > 100:
        digit = num % 10
        m_digit += str(digit)
        num //= 10
    rev_m = m_digit[::-1]
    if d[0] * d[1] == int(rev_m):
        return True
    else:
        return False
    
date = input()
print(is_magic(date))

## better solution:
def is_magic(date):
    d = date.split('.')
    day, month, year = int(d[0]), int(d[1]), int(d[2])

    return day * month == year % 100

## Панграммы

def is_pangram(text):
    t = text.lower()
    l = 'abcdefghijklmnopqrstuvwxyz'
    for i in l:
        if i not in t:
            return False
    
    return True

text = input()
print(is_pangram(text))

## Звездный треугольник

def draw_triangle():
    for i in range(8):
        print(' ' * (7 - i) + '*' * (1 + i * 2))

draw_triangle()

## Биномиальный коэффициент
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def compute_binom(n, k):
    if n == k == 1:
        return 1
    else:
        a = factorial(n)
        b = factorial(k)
        return(a / (b * factorial(n - k)))

n = int(input())
k = int(input())  

print(compute_binom(n, k))

## Число словами

def number_to_words(num):
    units = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    u = 0
    t = 0
    if 1 <= num <= 19:
        result = units[num - 1]
    elif num >= 20:
        if num % 10 == 0:
            result = tens[(num // 10) - 1]
        else:
            u = num % 10
            t = num // 10
            result = tens[t - 1] + ' ' + units[u - 1] 
    
    return result

n = int(input())
print(number_to_words(n))

## Numbers

import math

n = int(input())
a = math.log2(n)
b = math.ceil(a)
print(b)

## one-lane version:
import math

print(math.ceil(math.log2(int(input))))

## Passive-aggressive number guessing game

import random as r
r_num = r.randint(1, 100)

print('Добро пожаловать в числовую угадайку')

def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    else:
        return False

while True:
    num = input('Введите целое число от 1 до 100: ')
    if not is_valid(num):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

    digit = int(num)
    
    if digit < r_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif digit > r_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break

## Magic 8 ball

import random as r

answers = [ "Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова",
    "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже",
    "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы",
    "Лучше не рассказывать", "По моим данным - нет", "Определённо да",
    "Знаки говорят - да", "Сейчас нельзя предсказать",
    "Перспективы не очень хорошие", "Можешь быть уверен в этом", "Да",
    "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
greetings = print('Привет, ', input())

def valid(s):
    s = s[:-1]
    new_s = s.split(' ')
    for i in range(len(new_s)):
        if str(new_s[i]).isalpha():
            return True
        else:
            return False

while True:
    print('Я готов тебя выслушать...')
    question = input()
    if not valid(question):
        print('Извини, в ответах я ограничен,', 'Правильно задавай вопросы', sep = '\n')
        continue
    else:
        print(r.choice(answers))
        print('Хочешь продолжить?')
        a = input('Твой ответ...')
        if a == 'Да':
            continue
        else:
            print('Скоро увидимся')
            break

## Base Number System Conversion (BOH)

n = int(input())
b = bin(n)
o = oct(n)
h = hex(n)

print(b[2:], o[2:], h[2:].upper(), sep = '\n')

## Password generator

import random as r

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

amount = input('Количество паролей')
l = input('Длина пароля:')
dig_n = input('Включать ли цифры 0123456789? (y/n)')
l_n = input('Включать ли строчные буквы? (y/n)')
u_n = input('Включать ли прописные буквы? (y/n)')
s_n = input('Включать ли символы? (y/n)')
ex = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if dig_n == 'y':
    chars += digits
if l_n =='y':
    chars += lowercase_letters
if u_n == 'y':
    chars += uppercase_letters
if s_n == 'y':
    chars += punctuation
if ex == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i,'')

def generate_password(length, chars):
    password = ''
    for i in range(int(l)):
        password += r.choice(chars)
    return print(password)

for _ in range(int(amount)):
    generate_password(l, chars)

## На easy

a, b = int(input()), int(input())
print((a + b), (a - b), (a * b), (a / b), (a // b), (a % b), ((a ** 10 + b ** 10) ** 0.5), sep = '\n')

## Предикат делимости

def func(n1, n2):
    return n1 % n2 == 0

num1, num2 = int(input()), int(input())
if func(num1, num2):
    print('делится')
else:
    print('не делится')

## Шифр Цезаря

def caesar_encripter(char, k):
    ord_char = ord(char)
    if 65 <= ord_char <= 90:
        first_char = 65
        last_char = 90
        alphabet_power = 26
    elif 97 <= ord_char <= 122:
        first_char = 97
        last_char = 122
        alphabet_power = 26
    elif 1040 <= ord_char <= 1071:
        first_char = 1040
        last_char = 1071
        alphabet_power = 32
    elif 1072 <= ord_char <= 1103:
        first_char = 1072
        last_char = 1103
        alphabet_power = 32
    else:
        return(char)
    return chr(first_char + (ord(char) - first_char + k) % alphabet_power)

print('Покажи мне текст...')
text = input()
print('Где ключ?..')
key = int(input())

for i in range(len(text)):
    print(caesar_encripter(text[i], key), end = '')

## Индекс массы тела

def weight_index(w, h):
    w_i = w / h ** 2
    if w_i < 18.5:
        result = 'Недостаточная масса'
    elif w_i > 25:
        result = 'Избыточная масса'
    else:
        result = 'Оптимальная масса'
    return(result)

weight, height = float(input()), float(input())
print(weight_index(weight, height))

## Стоимость строки

l = input()
price = len(l) * 6
rub = price // 10
cop = price % 10 * 10
print(rub, 'р.', cop, 'коп.')

## Количество слов

l = input().split(' ')
print(len(l))

## Зодиак

zodiak = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
year = int(input())
y = year % 12
print(zodiak[y])

## Переворот числа

n = input()
if len(n) == 5:
    a = n[::-1]
    print(int(a))
elif len(n) == 6:
    a = n[0]
    b = n[:-6:-1]
    print(a, b, sep = '')  

## Standard American Convention

n = int(input())
print(f'{n:,}')

## Координатные четверти

def grafik(s):
    l = s.split(' ')
    x = int(l[0])
    y = int(l[1])
    result = 0
    if x > 0 and y > 0:
        result = 1
    elif x > 0 and y < 0:
        result = 4
    elif x < 0 and y < 0:
        result = 3
    elif x < 0 and y > 0:
        result = 2
    elif (x == 0 and y != 0) or (x != 0 and y == 0):
        result = 0
    return result

fst = 0
snd = 0
thd = 0
fth = 0

n = int(input())
for i in range(n):
    xy = input()
    result = grafik(xy)
    if result == 1:
        fst += 1
    elif result == 2:
        snd += 1
    elif result == 3:
        thd += 1
    elif result == 4:
        fth += 1
print('Первая четверть: ', fst)
print('Вторая четверть: ', snd)
print('Третья четверть: ', thd)
print('Четвертая четверть: ', fth)
##Better solution:
n = int(input())
count = [0, 0, 0, 0]
names = ['Первая четверть:', 'Вторая четверть:', 'Третья четверть:', 'Четвертая четверть:']
for _ in range(n):
    x, y = [int(num) for num in input().split()]
    if x > 0 and y > 0:
        count[0] += 1
    elif x < 0 and y > 0:
        count[1] += 1
    elif x < 0 and y < 0:
        count[2] += 1
    elif x > 0 and y < 0:
        count[3] += 1
for i in range(4):
    print(names[i], count[i])

## Больше предыдущего

s = input().split()
count = 0
for i in range(1, len(s)):
    if int(s[i]) > int(s[i - 1]):
        count += 1
    else:
        continue
print(count)

## Назад, вперёд и наоборот

s = input().split()
for i in range(0, len(s) - 1, 2):
    s[i], s[i + 1] = s[i + 1], s[i]
print(*s)

## Сдвиг в развитии

n = input().split()
last = n.pop()
print(last, *n)

## Различные элементы

n = input().split()
new_n = []
for i in range(len(n)):
    if n[i] not in new_n:
        new_n.append(n[i])
print(len(new_n))

## Произведение чисел
l = []
p_l = []

amount = int(input())

for _ in range(amount):
    l.append(int(input()))
p = int(input())

for i in range(0, len(l)):
    for j in range(0, len(l)):
        if i != j:
            a = l[j] * l[i]
            p_l.append(a)

print(p_l)
if p in p_l:
    print('ДА')
else:
    print('НЕТ')

## Rock/Paper/Scissors

def r_p_s(a, b):
    base = ['камень', 'ножницы', 'бумага']
    if (a == base[0] and b!= base[2]) or (a == base[1] and b != base[0]) or (a == base[2] and b != base[1]):
        result = a
    else:
        result = b
    return result

player_1, player_2 = input(), input()
if player_1 == player_2:
    print('ничья')
elif r_p_s(player_1, player_2) == player_1:
    print('Тимур')
else:
    print('Руслан')

## Орел и решка

results = input().split('О')
print(len(max(result)))

## Камень, ножницы, бумага, ящерица, Спок

def rock_paper_scissors_extended(gest1, gest2):
    base = ['камень', 'ножницы', 'бумага', 'ящерица', 'Спок']
    if gest1 == base[0] and (gest2 == base[1] or gest2 == base[3]):
        result = gest1
    elif gest1 == base[1] and (gest2 == base[2] or gest2 == base[3]):
        result = gest1
    elif gest1 == base[2] and (gest2 == base[0] or gest2 == base[4]):
        result = gest1
    elif gest1 == base[3] and (gest2 == base[2] or gest2 == base[4]):
        result = gest1
    elif gest1 == base[4] and (gest2 == base[0] or gest2 == base[1]):
        result = gest1
    else:
        result = gest2
    return result

g1, g2 = input(), input()
if g1 == g2:
    print('ничья')
elif rock_paper_scissors_extended(g1, g2) == g1:
    print('Тимур')
else:
    print('Руслан')

## find elements p in lane

n = int(input())
r = []
p = ['a', 'n', 't', 'o', 'n']
for i in range(n):
    lane = input()
    f_index = 0
    for j in lane:
        if j == p[f_index]:
            f_index += 1
            if f_index == len(p):
                r.append(i + 1)
                break
print(r)
##better solution:
n = int(input())
for i in range(n):
    seq = ["a", "n", "t", "o", "n"]
    s = list(input())
    while seq and s:
        if seq[0] == s[0]:
            seq.pop(0)
            s.pop(0)
        else:
            s.pop(0)
    if not seq:
        print(i + 1, end=" ")

## Вложенные списки

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

print(list1)

## 

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)

##

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = 0
for i in range(len(list1)):
    for j in list1[i]:
        if j > maximum:
            maximum = j
print(maximum)

##

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for i in range(len(list1)):
    list1[i].reverse()
print(list1)

##

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in range(len(list1)):
    counter += len(list1[i])
    total += sum(list1[i])
print(total/counter)

## Список по образцу 1

n = int(input())
l = []
for _ in range(n):
    elem = [i for i in range(1, n + 1)]
    l.append(elem) 
    print(elem, sep = '\n')

## Список по образцу 2

n = int(input())
l = []
for i in range(1, n + 1):
    elem = [j for j in range(1, i + 1)]
    l.append(elem) 
    print(elem, sep = '\n')

## Треугольник Паскаля 1
    
def pascal(num):
    if num == 0:
        return[1]
    
    triangle = []
    for row in range(num):
        cur_row = []
        for elem in range(row + 1):
            if elem == 0 or elem == row:
                cur_row.append(1)
            else:
                cur_row.append(triangle[row - 1][elem - 1] + triangle[row - 1][elem])
        triangle.append(cur_row)
    return triangle[num - 1]

pascal(int(input()))

##corect solution:
def pascal(n):
    if n == 0:
        return [1]
    row = [1]
    for i in range(1, n + 1):
        new_row = [1]
        for j in range(1, i):
            new_row.append(row[j - 1] + row[j])
        new_row.append(1)
        row = new_row
    return row

print(pascal(int(input())))

n = int(input())
for i in range(n):
    print(*pascal(i))
    

## Упаковка дубликатов

l = input().split()
packed_l = []

temp = [l[0]]
for i in range(1, len(l)):
    if l[i] == l[i - 1]:
        temp.append(l[i])
    else:
        packed_l.append(temp)
        temp = [l[i]]
packed_l.append(temp)

print(packed_l)

## chunked

def chunked(l, n):
    new_l = [] 
    for i in range(0, len(l), n):
        new_l.append(l[i:i + n])
    return(new_l)

s = input().split()
number = int(input())
print(chunked(s, number))

## Matrix

n, m = int(input()), int(input())
matrix = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = input()
for i in range(n):
    print(*matrix[i], end = '\n')

## Matrix2

n, m = int(input()), int(input())
matrix = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = input()
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = ' ')
    print()

print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end = ' ')
    print()

## След квадратной матрицы

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

def matrix_trace(rows, matrix):
    cols = rows
    m_trace = 0
    for r in range(rows):
        for c in range(cols):
            if r == c:
                m_trace += matrix[r][c]  
                
    return m_trace

print(matrix_trace(n, matrix))


## Больше среднего
    
rows = int(input())
matrix = []
for _ in range(rows):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)

for lane in matrix:
    above_avg = 0
    avg_in_row = sum(lane) / len(lane)
    for num in lane:
        if num > avg_in_row:
            above_avg += 1
    print(above_avg)

## Max in area

## matrix = [[int(i) for i in input().split()] for _ in range(int(input()))]

rows = int(input())
matrix = []
for _ in range(rows):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
mx = -10 ** (9)
for row in range(rows):
    for col in range(len(matrix[row])):
        if row >= col:
            if matrix[row][col] > mx:
                mx = matrix[row][col]
print(mx)

## Max in area 2

rows = int(input())
matrix = []
for _ in range(rows):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
mx = matrix[0][0]
for row in range(rows):
    for col in range(len(matrix[row])):
        if (row >= col and row <= (rows - 1 - col)) or (row <= col and row >= (rows - 1 - col)):
            if matrix[row][col] > mx:
                mx = matrix[row][col]
print(mx)

## Sum of quarters

rows = int(input())
matrix = []
for _ in range(rows):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)

q_left, q_up, q_right, q_down = 0, 0, 0, 0

for i in range(rows):
    for j in range(len(matrix[i])):
        if i > j and i < (rows - 1 - j):
            q_left += matrix[i][j]
        elif i > j and i > (rows - 1 - j):
            q_down += matrix[i][j]
        elif i < j and i > (rows - 1 - j):
            q_right += matrix[i][j]
        elif i < j and i < (rows - 1 - j):
            q_up += matrix[i][j]

print(f'Верхняя четверть: {q_up}', f'Правая четверть: {q_right}', f'Нижняя четверть: {q_down}', f'Левая четверть: {q_left}', sep='\n')

## Multiplication table

n, m = int(input()), int(input())
mult = []
for i in range(n):
    lane = [i * j for j in range(m)]
    mult.append(lane)

for x in range(n):
    for y in range(m):
        print(str(mult[x][y]).ljust(3), end = '')
    print()

## Max in the table

n, m = int(input()), int(input())
matrix = []
for i in range(n):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)

mx = matrix[0][0]
a = 0
b = 0

for x in range(n):
    for y in range(m):
        if int(matrix[x][y]) > int(mx):
            mx = matrix[x][y]
            a = x
            b = y

print(a, b)

## Обмен столбцов

n, m = int(input()), int(input())
matrix = []
for i in range(n):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
i, j = map(int, input().split())

for x in range(n):
    matrix[x][i], matrix[x][j] = matrix[x][j], matrix[x][i]

for lane in matrix:
    print(*lane)

## Симметричность матрицы

n = int(input())
matrix = []
for _ in range(n):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
is_symmetric = True
for x in range(n):
    for y in range(n):
        if matrix[x][y] != matrix[y][x]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print('YES')
else:
    print('NO')

## Обмен диагоналей

n = int(input())
matrix = []
for _ in range(n):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
for x in range(n):
    for y in range(n):
        if x == y:
            matrix[x][y], matrix[x][(n - x - 1)] = matrix[x][(n - x - 1)], matrix[x][y]
for x in range(n): 
    for y in range(n):
        print(matrix[x][y], end=' ')
    print()
##correct solution:
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row)

## Сложение матриц

n, m = map(int, input().split())

matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

input()

matrix2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

result_matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(row)

for row in result_matrix:
    print(*row)

## Умножение матриц

n, m = map(int, input().split())

matrix1 = []
matrix2 = []

for _ in range(n):
    row1 = list(map(int, input().split()))
    matrix1.append(row1)

input()

m, k = map(int, input().split())


for _ in range(m):
    row2 = list(map(int, input().split()))
    matrix2.append(row2)

matrix3 = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for h in range(m):
            matrix3[i][j] += matrix1[i][h] * matrix2[h][j]

for row in matrix3:
    print(*row)

## Возведение матрицы в степень

rows = int(input())
matrix = []
matrix_result = [] 

for _ in range(rows):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
    matrix_result.append(lane.copy())

power = int(input()) 
 
while power > 1:
    temp_result = [[0]*rows for _ in range(rows)]
    for i in range(rows):
        for j in range(rows):
            for h in range(rows):
                temp_result[i][j] += matrix_result[i][h] * matrix[h][j]
    matrix_result = temp_result
    power -= 1

for row in matrix_result:
    print(*row)

## Зеркальное отображение

dimension = int(input())
matrix = []
matrix1 = []

for _ in range(dimension):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)

matrix1 = matrix[::-1]

for i in matrix1:
    print(*i)

## Поворот матрицы

dimension = int(input())
matrix = []
matrix1 = []

for _ in range(dimension):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)

matrix1 = matrix[::-1]

for i in range(dimension):
    for j in range(dimension):
        print(matrix1[j][i], end = ' ')
    print()

## Магический квадрат
   
def magic(n, matrix):
    cor_nums = list(range(1, n ** 2 + 1))
    tested_nums = []
    for lane in matrix:
        tested_nums.extend(lane)
    tested_nums.sort()
    if tested_nums != cor_nums:
        return 'NO'
    
    lanes = matrix.copy()
    
    cols = []
    for j in range(n):
        cur_col = []
        for i in range(n):
            cur_col.append(matrix[i][j])
        cols.append(cur_col)

    diags = [[], []]
    for i in range(n):
        diags[0].append(matrix[i][i])
        diags[1].append(matrix[i][n - 1 - i])
    
    all_n = lanes + cols + diags
    max_sum = sum(all_n[0])
    min_sum = sum(all_n[0])
    for lane in all_n:
        max_sum = max(max_sum, sum(lane))
        min_sum = min(min_sum, sum(lane))
    if max_sum != min_sum:
        return "NO"
    return "YES"

n = int(input())
matrix = []
for _ in range(n):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)

print(magic(n, matrix))

## Ходы коня

matrix = [['.']*8 for _ in range(8)]
field_col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
field_row = ['8', '7', '6', '5', '4', '3', '2', '1']

loc = input()

y = field_col.index(loc[0])
x = field_row.index(loc[1])

matrix[x][y] = 'N'

for i in range(8):
    for j in range(8):
        if (abs(x - i) == 1 and abs(y - j) == 2) or (abs(x - i) == 2 and abs(y - j) == 1):
            matrix[i][j] = '*'

for i in range(8):
    print(*matrix[i], end = '\n')

## Шахматная доска

params = input().split()
n = int(params[0])
m = int(params[1])
chess_board = ['.' * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
            print(chess_board[i][j].replace('.', '*'), end = ' ')
        else:
            print(chess_board[i][j], end = ' ')
    print()

## Заполнение 1

params = input().split()
n = int(params[0])
m = int(params[1])
matrix = [[0] * m for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        count += 1
        matrix[i][j] = count
    
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end = '')
    print()

## Заполнение 2

params = input().split()
n = int(params[0])
m = int(params[1])
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i + j * n + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end = '')
    print()

## Заполнение 3
    
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1:
            matrix[i][j] = 1
        print(matrix[i][j], end = ' ')
    print()

## Заполнение 4

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1:
            matrix[i][j] = 1
        if i < j and i < n - 1 - j:
            matrix[i][j] = 1
        if i > j and i > n - 1 - j:
            matrix[i][j] = 1
        print(matrix[i][j], end = ' ')
    print()

## Побочная диагональ
    
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n - j - 1:
            matrix[i][j] = 1
        if i > n - 1 - j:
            matrix[i][j] = 2
        print(matrix[i][j], end = ' ')
    print()

## Заполнение 5

params = input().split()
n = int(params[0])
m = int(params[1])
matrix = []
lane = list(range(1, m + 1))

for i in range(n):
    matrix.append(lane)
    lane = lane[1:] + [lane[0]]

for i in matrix:
    print(*i)

## Заполнение змейкой

params = input().split()
n = int(params[0])
m = int(params[1])
matrix = []

count = 0

for i in range(n):
    for j in range(m):
        count += 1
        matrix[i][j] = count
for i in matrix:
    if i % 2 == 0:
        print(i[:-1])
    else:
        print(i)

## Заполнение диагоналями

params = input().split()
n = int(params[0])
m = int(params[1])
matrix = [[0] * m for _ in range(n)]
##lane = [x for x in range(n * m)]
temp = 1
for i in range(n + m):
    for j in range(n):
        for k in range(m):
            if j + k == i:
                matrix[j][k] = temp
                temp += 1   

## Заполнение спиралью

def spiral(rows, cols):
    matrix = [[0] * cols for _ in range(rows)]
    num = 1
    top_row = 0
    bottom_row = rows - 1
    left_col = 0
    right_col = cols - 1

    while top_row <= bottom_row and left_col <= right_col:

        for i in range(left_col, right_col + 1):
            matrix[top_row][i] = num
            num +=1
        top_row += 1

        for i in range(top_row, bottom_row + 1):
            matrix[i][right_col] = num
            num += 1
        right_col -= 1

        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                matrix[bottom_row][i] = num
                num += 1
            bottom_row -= 1

        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                matrix[i][left_col] = num
                num += 1
            left_col += 1

    for i in matrix:
        print(*i)
    print()
        

params = input().split()
n = int(params[0])
m = int(params[1])
spiral(n, m)

## Максимальный в области 2

n = int(input())
matrix = []
for i in range(n):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
mx = -10 ** (9)
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:
            if matrix[i][j] > mx:
                mx = matrix[i][j]
print(mx)

## Транспонирование матрицы

n = int(input())
matrix = []
new_matrix = [[0] * n for _ in range(n)]

for _ in range(n):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
    
for i in range(n):
    for j in range(n):
        new_matrix[i][j] = matrix[j][i]
        
for i in range(n):
    for j in range(n):
        print(new_matrix[i][j], end = ' ')
    print()

## Снежинка

n = int(input())
matrix = ['.' * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j or i + j + 1 == n) or (i == n //2 or j == n // 2):
            print(matrix[i][j].replace('.', '*'), end = ' ')
        else:
            print(matrix[i][j], end = ' ')
    print()


## Симметричная матрица

n = int(input())
matrix = []
for _ in range(n):
    lane = [int(num) for num in input().split()]
    matrix.append(lane)
is_symmetric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n-j-1][n-i-1]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print('YES')
else:
    print('NO')

## Латинский квадрат

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

test_lane = list(range(1, n + 1))

flag = True

for i in range(n):
    h_nums = sorted(matrix[i])
    v_nums = sorted(matrix[j][i] for j in range(n))

    if h_nums != test_lane or v_nums != test_lane:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')


## Ходы ферзя
            
matrix = [['.']*8 for _ in range(8)]
field_col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
field_row = ['8', '7', '6', '5', '4', '3', '2', '1']

loc = input()

y = field_col.index(loc[0])
x = field_row.index(loc[1])

for i in range(8):
    for j in range(8):
        if i == x or j == y or (i + j == x + y) or (j - i == y - x):
            matrix[i][j] = '*'

matrix[x][y] = 'Q'

for i in range(8):
    print(*matrix[i], end = '\n')

## Каждый n-ый элемент
def chunked(l, n):
    new_l = [] 
    for i in range(0, n):
        new_l.append(l[i::n])
    return(new_l)

s = input().split()
number = int(input())
print(chunked(s, number))

## Tuples

tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [tuples[i] for i in range(len(tuples)) if len(tuples[i]) > 0]
print(non_empty_tuples)

tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples]
print(new_tuples)

numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
count = 1
for i in range(len(numbers)):
    count*= numbers[i]
print(count)

## Tuples

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
temp = list(poet_data)
temp[2] = 'Москва'
poet_data = tuple(temp) 

print(poet_data)

## 

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
avg = []
for i in numbers:
    temp = 0
    temp = sum(i)/len(i)
    avg.append(temp)
print(avg)

## Вершина параболы

def vertex_coordinates(a, b, c):

    x = -b / (2 * a)
    y = (4 * a * c - b ** 2) / (4 * a)

    return(x, y)

a, b, c = int(input()), int(input()), int(input())
print(vertex_coordinates(a, b, c))

## Конкурсный отбор

n = int(input())

students = []
for i in range(n):
    temp = input()
    students.append(temp)
best_students = []
for student in students:
    grade = int(student[-1])
    if grade in (4, 5):
        best_students.append(student)
        
print(*students, sep = '\n')
print()
print(*best_students, sep = '\n')
## better version:
students = [tuple(input().split()) for _ in range(int(input()))]
for student in students:
    print(*student)
print()
for name, grade in students:
    if int(grade) > 3:
        print(name, grade)

## Последовательность Трибоначчи

n = int(input())
F1 = 1
F2 = 1
F3 = 1
for i in range(n):
    print(F1, end=' ')
    F1, F2, F3 = F2, F3, F1+F2+F3

## Множества

##море
n = int(input())
##деревня
m = int(input())
##горы
k = int(input())

x = int(input()) ##(n + m)
y = int(input()) ##(m + k)

z = int(input())

students = z + (n - x) +  (k - y) + (m - x - y) + x + y

print(students)

## Множества

n = int(input("Количество учеников, прочитавших первую книгу: "))
m = int(input("Количество учеников, прочитавших вторую книгу: "))
k = int(input("Количество учеников, прочитавших третью книгу: "))
x = int(input("Количество учеников, прочитавших первую или вторую, или обе книги: "))
y = int(input("Количество учеников, прочитавших вторую или третью, или обе книги: "))
z = int(input("Количество учеников, прочитавших первую и третью, или хотя бы одну из этих двух книг: "))
t = int(input("Количество учеников, полностью выполнивших задание: "))
a = int(input("Общее количество учеников в 10 классе: "))

b12 = n + m - t - x
b23 = m + k - t - y
b31 = k + n - t - z 

two_books = b12 + b23 + b31

b1 = n - t - b12 - b31
b2 = m - t - b12 - b23
b3 = k - t - b31 - b23

one_book = b1 + b2 + b3

zero_books = a - one_book - two_books - t

print(one_book, two_books, zero_books, sep = '\n')

##

numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
s = 0
for n in numbers:
    s += n ** 2

print(s)

##

fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
sort_fruits = sorted(fruits, reverse = True)
print(*sort_fruits, sep = '\n')

## Количество различных символов

print(len(set(input())))

## 

s = input()
new_s = set(s,)
if len(s) == len(new_s):
    print('YES')
else:
    print('NO')

## 

first, second = input(), input()
new = first + second
if len(set(new)) == 10:
    print('YES')
else:
    print('NO')

## Одинаковые наборы

first, second = input(), input()
if len(set(first)) == len(set(second)) and sorted(set(first)) == sorted(set(second)):
    print('YES')
else:
    print('NO')

##

lane = input().split()
etalon = set(lane[0])
count = 0
for i in range(len(lane)):
    if len(set(lane[i])) == len(etalon) and sorted(set(etalon)) == sorted(set(lane[i])):
        count += 1
if count == len(lane):
    print('YES')
else:
    print('NO')

## Уникальные символы 1

for i in range(int(input())):
    print(len(set(input().lower())))
   
## Уникальные символы 2
    
s = ''
for i in range(int(input())):
    a = input().lower()
    s += a

print(len(set(s)))

## Количество слов в тексте

s = input().lower().split()
ignored_char = ['.', ',', ';', ':', '-', '?', '!']

for i in range(len(s)):
    word = s[i]
    if not word.isalpha():
        for j in word:
            if j in ignored_char:
                word = word.replace(j, '')
        s[i] = word

myset = set()
for i in range(len(s)):
    myset.add(s[i])
    
print(len(myset))

## Числа

numbers = [int(i) for i in input().split()]

print(numbers)
print(type(numbers[0]))
myset = set()

for i in range(len(numbers)):
    if numbers[i] not in myset:
        print('NO')
        myset.add(numbers[i])
    else:
        print('YES')

## intersection 1
        
lane1, lane2 = set(input().split()), set(input().split())
lane3 = lane1.intersection(lane2)
print(len(lane3))

## intersection 2

lane1, lane2 = set(input().split()), set(input().split())

lane3 = lane1.intersection(lane2)
response = list(lane3)
for i in range(len(response)):
    response[i] = int(response[i])

print(*sorted(response))

## difference

lane1, lane2 = set(input().split()), set(input().split())
lane3 = lane1.difference(lane2)
response = list(lane3)
for i in range(len(response)):
    response[i] = int(response[i])

print(*sorted(response))

## Общие цифры

n = int(input())
s = set(input())
for i in range(n - 1):
    s.intersection_update((input()))

print(*sorted(s))

## Одинаковые цифры

s1, s2 = set(input()), set(input())
if s1.isdisjoint(s2):
    print('NO')
else:
    print('YES')

## Все цифры

s1, s2 = set(input()), set(input())
print(('NO', 'YES')[s1.issuperset(s2)])

## Урок информатики

notes = []
for i in range(3):
    notes.append(set((input().split())))
response = notes[0] & notes[1] - notes[2]
r = list(response)
r = [int(r[i]) for i in range(len(r))]
print(*sorted(r, reverse = True))

## Set Generator 1

items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
r = items
r = {str(r[i]) for i in range(len(r))}
temp = list(r)
answer = [int(temp[i]) for i in range(len(temp))]
print(*sorted(answer))
## better solution:
items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
myset = {int(i) for i in items}
print(*sorted(myset))

## Set Generator 2

words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
s = str(words)
resp = ''
for i in range(len(words)):
    resp += words[i][0].lower()

myset = {resp[i] for i in range(len(resp))}
print(*sorted(myset))

## Урок математики

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

resp = (set1 | set2 | set3) - (set1 & set2 & set3)

print(*sorted(resp))

## Урок биологии

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

all = {int(i) for i in range(11)}
resp = all - (set1 | set2 | set3)

print(*sorted(resp))

## Урок физики

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

resp = set3 - (set1 | set2)

print(*sorted(resp, reverse = True))

## 

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
myset = {word.lower().strip('.,;:-?!()') for word in sentence.split() if len(word) < 4}
print(*sorted(myset))

## 

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
myset = {file.lower() for file in files if file.lower().endswith('.png')}

print(*sorted(myset))

## Домашнее задание

n, m, k, p = int(input()), int(input()), int(input()), int(input())
resp = (m - p) + p + (k - p)
print(resp)

## Восход

data = input().split()
myset = {int(data[i]) for i in range(len(data))}
print(len(data) - len(myset))

## Города

n = int(input())
db = []
for i in range(n):
    db.append(input().lower().split())
city = input().lower().split()

if city in db:
    print('REPEAT')
else:
    db.append(city)
    print('OK')

## Книги на прочтение

m, n = int(input()), int(input())
home, school = [], []

for i in range(m):
    home.append(input())
for j in range(n):
    school.append(input())
    if school[j] in home:
        print('YES')
    else:
        print('NO')

## Странное увлечение

page1, page2 = set(input().split()), set(input().split())
page3 = list(page1 & page2)
page3 = [int(page3[i]) for i in range(len(page3))]
if len(page3) > 0:
    print(*sorted(page3, reverse = True))
else:
    print('BAD DAY')

## Онлайн-школа 1

shown = {int(i) for i in input().split()}
remembered = {int(i) for i in input().split()}

if shown == remembered:
    print('YES')
else:
    print('NO')

## Онлайн-школа 2

m, i = int(input()), int(input())
math, info = [], []

for j in range(m):
    math.append(input())
for j in range(i):
    info.append(input())
math_only = set(math) - set(info)
print(len(math_only))

## Онлайн-школа 3

m, i = int(input()), int(input())
math, info = [], []

for j in range(m):
    math.append(input())
for j in range(i):
    info.append(input())
one_only = set(math) ^ set(info)
if len(one_only) > 0:
    print(len(one_only))
else:
    print('NO')

## Онлайн-школа 4

list1 = {i for i in input().split()}
list2 = {i for i in input().split()}
print(*sorted(list1 | list2))

## Онлайн-школа 5

m, i = int(input()), int(input())
students = [input() for _ in range(m + i)]
myset = set(students)

if len(students) == len(myset):
    print(len(students))
elif (len(students) / 2) == len(myset):
    print('NO')
else:
    resp = len(students) - ((len(students) - len(myset)) * 2)
    print(resp)

## Онлайн-школа 6

m = int(input())
students = []
for i in range(m):
    for j in range(int(input())):
        students.append(input())
good_students = set()
for student in students:
    if students.count(student) == m:
        good_students.add(student)
print(*sorted(good_students), sep = '\n')

## Dictionaries!

my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(min(my_dict) + max(my_dict))

##

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

resp1 = []
for user in users:
    if user['phone'][-1] == '8':
        resp1.append(user['name'])
print(*sorted(resp1))

resp2 = []
for user in users:
    if 'email' in user and user['email'] == '':
        resp2.append(user['name'])
    elif 'email' not in user:
        resp2.append(user['name'])
print(*sorted(resp2))
## or:
resp2 = [user['name'] for user in users if 'email' not in user or user['email'] == '']
print(*sorted(resp2))

## Строковое представление

mydict = {'0': 'zero',
          '1': 'one',
          '2': 'two',
          '3': 'three',
          '4': 'four',
          '5': 'five',
          '6': 'six',
          '7': 'seven',
          '8': 'eight',
          '9': 'nine'}

data = input()

for i in data:
    print(mydict[i], end = ' ')

## Информация об учебных курсах

d = {
    'CS101': {'audience_number': '3004', 'teacher': 'Хайнс', 'time': '8:00'}, 
    'CS102': {'audience_number': '4501', 'teacher': 'Альварадо', 'time': '9:00'}, 
    'CS103': {'audience_number': '6755', 'teacher': 'Рич', 'time': '10:00'}, 
    'NT110': {'audience_number': '1244', 'teacher': 'Берк', 'time': '11:00'}, 
    'CM241': {'audience_number': '1411', 'teacher': 'Ли', 'time': '13:00'}
}

n = input()

r = f"{n}: {d[n]['audience_number']}, {d[n]['teacher']}, {d[n]['time']}"
print(r)

## Набор сообщений (Nokia 3310)

message = input().upper()

d = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' '}

for letter in message:
    for key, values in d.items():
        if letter in values:
            count = values.index(letter) + 1
            print(count * key, end = '')
            break           

## Код Морзе

message = input().upper()

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
morse_code = dict(zip(letters, morse))

for letter in message:
    if letter in morse_code:
        print(morse_code[letter], end = ' ')

## 

result = {i: i ** 2 for i in range(1, 16)}
## or:
result = {}
for i in range(1, 16):
    result.setdefault(i, i ** 2)

## 

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = {}

result.update(dict2)
result.update(dict1)

for elem in result:
    if elem in dict1 and elem in dict2:
        result[elem] = dict1[elem] + dict2[elem]

##

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
mylist = [i for i in text]
result = {}

for elem in mylist:
    result[elem] = result.get(elem, 0) + 1

##

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
mylist = s.split()
mydict = {}
for elem in mylist:
    mydict[elem] = mydict.get(elem, 0) + 1
resp = []
temp = max(mydict.values())

for key, value in mydict.items():
    if value == temp:
        resp.append(key)

print(min(resp))

## распаковка кортежа - множественное присваивание

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for pet, first_name, second_name, age in pets:
    owner = (first_name, second_name, age)

    result.setdefault(owner, []).append(pet)

## Самое редкое слово

text = input().lower().split()
text = [i.strip('.,!?:;-') for i in text]

mydict = {}

for word in text:
    mydict[word] = mydict.get(word, 0) + 1

resp = []
temp = min(mydict.values())

for key, value in mydict.items():
    if value == temp:
        resp.append(key)
    
print(min(resp))

## Исправление дубликатов

ids = input().split()
temp = 0
resp = []
for i in range(len(ids)):
    temp = ids[:i + 1].count(ids[i])
    if temp > 1:
        resp.append(ids[i] + '_' + str(temp - 1))
    else:
        resp.append(ids[i])            

print(*resp)

## Словарь программиста

n = int(input())
mydict = {}
for i in range(n):
    key, value = input().split(': ')
    mydict[key.lower()] = value

m = int(input())
inspected = []
for i in range(m):
    inspected.append(input().lower())

for elem in inspected:
    print(mydict.get(elem, 'Не найдено'))

## Анаграммы 1

test1, test2 = list(input()), list(input())
mydict1 = {}
mydict2 = {}

for elem in test1:
    mydict1[elem] = mydict1.get(elem, 0) + 1
    
for elem in test2:
    mydict2[elem] = mydict2.get(elem, 0) + 1

if mydict1 == mydict2:
    print('YES')
else:
    print('NO')

## Анаграммы 2

lane1, lane2 = input().lower().split(), input().lower().split()
lane1 = [i.strip('.,!?:;-') for i in lane1]
lane2 = [i.strip('.,!?:;-') for i in lane2]

mydict1 = {}
mydict2 = {}

for elem in lane1:
    for i in elem:
        mydict1[i] = mydict1.get(i, 0) + 1
        
for elem in lane2:
    for i in elem:
        mydict2[i] = mydict1.get(i, 0) + 1

if sorted(mydict1) == sorted(mydict2):
    print('YES')
else:
    print('NO')
## better-faster-stronger:
lane1 = [i for i in input().lower() if i.isalpha()]
lane2 = [i for i in input().lower() if i.isalpha()]
print('YES' if sorted(lane1) == sorted(lane2) else 'NO')

## Словарь синонимов

n = int(input())
mydict = {}

for i in range(n):
    key, value = input().split(' ')
    mydict[key] = value
test = input()

for key, value in mydict.items():
    if test in value and value == test:
        print(key)
    elif test in key and key == test:
        print(value)

## Страны и города

d = {i[0]: i[1:] for i in [input().split() for _ in range(int(input()))]}
inspect = [input().split() for i in range(int(input()))]

for city in inspect:
    for key, value in d.items():
        if city in value:
            print(key)

## Телефонная книга

dct = {}
for _ in range(int(input())):
    phone, name = input().lower().split()
    dct.setdefault(name, []).append(phone)
for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))

## Секретное слово

secret = input()
secret_dict = {}
for elem in secret:
    secret_dict[elem] = secret_dict.get(elem, 0) + 1

n = int(input())
dict = {}
for i in range(n):
    key, value = input().split(': ')
    dict[int(value)] = key

resp = []

for i in secret:
    resp.append(dict[secret_dict[i]])
    
print(*resp, sep = '')

## dict generator

numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]

result = {i: numbers[i] ** 2 for i in range(len(numbers))}

##

colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}

result = {key: value for key, value in colors.items() if value}

##

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {value: key for key, value in months.items()}

##

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

result = {int(value): key for value, key in [l.split(':') for l in s.split()]}

##

numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {k: [num for num in range(1, k + 1) if k % num == 0] for k in numbers}
print(result)

##

words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {word: [ord(char) for char in word] for word in words}

##

letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]

result = {k: v for k, v in letters.items() if k not in remove_keys}

##

students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}

result = {k: v for k, v in students.items() if students[k][0] > 167 and students[k][1] < 75}

##

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]

result = {i[0]: i[1:] for i in tuples}

##

student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013'] 
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'] 
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_names))]
## using zip:
result = [{a: {b: c}} for a, b, c in zip(student_ids, student_names, student_grades)]

## Проверь никнейм

name = input()

if name[0] == '@' and len(name) <= 15 and len(name) >= 5 and name.lower() == name:
    if name[1:].isalnum():
        print('Correct')
    else:
        print('Incorrect')
else:
    print('Incorrect')

##

my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
my_dict = {k: [i for i in my_dict[k] if i <= 20] for k, v in my_dict.items()}

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
resp = []
temp = ''
for k, v in emails.items():
    for i in v:
        temp = i + '@' + k
        resp.append(temp)
        temp = ''
print(*sorted(resp), sep = '\n')

## DNA

c_rule = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
test_dna = input()
test_rna = {i: c_rule[test_dna[i]] for i in range(len(test_dna))}
for v in test_rna.values():
    print(v, end = '')

## Порядковый номер

s = input().split()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
    print(d[i], end = ' ')
## or:
test = input().split()
temp = 0
resp = []
for i in range(len(test)):
    temp = test[:i + 1].count(test[i])
    resp.append(temp)
print(*resp)

## Scrabble

word = input()
d = {
    "AEILNORSTU": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10
}

result = 0
for i in word:
    for k, v in d.items():
        if i in k:
            result += d[k]
print(result)

## query string

def build_query_string(params):
    resp = []
    
    for k, v in sorted(params.items()):
        resp.append(str(k) + '=' + str(v))
    return '&'.join(resp)

## merge

def merge(values):
    resp = {}
    for i in values:
        for k, v in i.items():
            resp.setdefault(k, set()).add(v)
    return resp

##

operation_dict = {'execute': 'X', 'read': 'R', 'write': 'W'}

n = int(input())
allowed_operations = {}
for _ in range(n):
    inputs = input().split()
    filename = inputs[0]
    operations = set(inputs[1:])
    allowed_operations[filename] = operations

m = int(input())
for _ in range(m):
    operation, filename = input().split()
    if filename in allowed_operations and operation_dict.get(operation) in allowed_operations[filename]:
        print("OK")
    else:
        print("Access denied")

## e-shopping

n = int(input())
client, item, amount = [], [], []
for i in range(n):
    temp = input().split()
    client.append(temp[0])
    item.append(temp[1])
    amount.append(int(temp[2]))

checkout = {}
for c, i, a in zip(client, item, amount):
    if c in checkout:
        checkout[c].append((i, a))
    else:
        checkout[c] = [(i, a)]

for c, p in sorted(checkout.items()):
    print(c + ":")
    for item, amount in sorted(p):
        print(f"{item} {amount}")
## correct solution:
data = {}

for _ in range(int(input())):
    name, product, count = input().split()
    data.setdefault(name, {})
    data[name][product] = data[name].get(product, 0) + int(count)
    
for person, products in sorted(data.items()):
    print(f'{person}:')
    for product, count in sorted(products.items()):
        print(product, count)

## Random coin

import random

n = int(input())
for i in range(n):
    resp = random.randint(1, 2)
    if resp == 1:
        print('Орел')
    else:
        print('Решка')

## Random dice

import random

n = int(input()) 
for i in range(n):
    print(random.randrange(1, 6))

## Pass generator

import random
length = int(input()) 
base = []
new_pass = ''
for i in range(length):
    base = list(chr(random.randrange(65, 90))) + list(chr(random.randrange(97, 122)))
    new_pass += base[random.randrange(0, 1)]
print(new_pass)

##

import random

nums = []

for i in range(7):
    temp = 0
    temp = random.randrange(1, 49)
    nums.append(temp)

print(*sorted(nums))

##
import random

def generate_ip():
    
    ip = '.'.join([str(random.randrange(0, 255)) for _ in range(4)])
    return ip

print(generate_ip())  

## Почтовый индекс в Латверии

import random

def generate_index():
    ind0 = chr(random.randrange(65, 90)) + chr(random.randrange(65, 90)) + str(random.randrange(0, 9)) + str(random.randrange(0, 9))
    ind1 = str(random.randrange(0, 9)) + str(random.randrange(0, 9)) + chr(random.randrange(65, 90)) + chr(random.randrange(65, 90))
    latveria_index = ind0 + '_' + ind1
    
    return latveria_index

print(generate_index())

## shuffle)

import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

random.shuffle(matrix)

##

import random

myset = set()
while len(myset) < 100:
    temp = random.randrange(1000000, 9999999)
    myset.add(temp)

print(*myset, sep = '\n')

##

import random

word = input()
mylist = list(word)
random.shuffle(mylist)

print(*mylist, sep = '')

## Bingo)

import random

bingo_card = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        if i == j == 2:
            bingo_card[i][j] = 0
        else:
            bingo_card[i][j] = random.randrange(1, 75)

for i in range(5):
    for j in range(5):
        print(str(bingo_card[i][j]).ljust(3), end = '')
    print()  
##
import random

bingo_card = [[0] * 5 for _ in range(5)]

temp = [str(i) for i in range(1, 76)]
random.shuffle(temp)
resp = random.sample(temp, 25)

for i in range(5):
    for j in range(5):
        bingo_card[i][j] = str(temp.pop()).ljust(3)

bingo_card[2][2] = str(0).ljust(3)
for i in bingo_card:
    print(*i, sep = '')

##

import random
import string

def generate_password(length):

    base = []
    base.append(string.ascii_letters)
    base.append(string.digits)
    restricted = ['l', 'I', '1', 'o', 'O', '0']

    b = ''
    for i in base:
        for j in i:
            if j not in restricted:
                b += str(j)
        
    pwd = ''
    pwd = random.sample(b, length)

    return pwd

def generate_passwords(count, length):

    for _ in range(count):
        print(*generate_password(length), sep = '')

n, m = int(input()), int(input())
generate_passwords(n, m)
## faster-better with string and set data type:
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    restricted = {'l', 'I', '1', 'o', 'O', '0'}
    available_chars = ''.join(c for c in characters if c not in restricted)
    return ''.join(random.choice(available_chars) for _ in range(length))

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n, m)

## Тайный друг

import random

students = []
for i in range(int(input())):
    students.append(input())

for i in range(len(students)):
    print(students[i], '-', students[i - 1])

## Генератор паролей 2

import random
import string

def generate_password(length):
    f = False
    chars = string.ascii_letters + string.digits
    restricted = {'l', 'I', '1', 'o', 'O', '0'}
    available_chars = ''.join(c for c in chars if c not in restricted)

    upper = set(string.ascii_uppercase)
    lower = set(string.ascii_lowercase)
    digit = set(string.digits)

    while not f:
        temp_list = list(available_chars)
        random.shuffle(temp_list)
        pwd = ''.join(temp_list[:length])
        temp = set(pwd)
        if len(temp & upper) > 0 and len(temp & lower)  > 0 and len(temp & digit) > 0:
            f = True
            
    return pwd

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
generate_passwords(n, m)

## Monte Carlo Simulation

import random

n = 10**6
s0 = 16
k = 0

for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if -2 <= x <= 2 and -2 <= y <= 2 and (x**3 + y**4 + 2) >= 0 and (3 * x + y** 2) <= 2:
        k += 1

print((k / n) * s0)

## Monte Carlo Simulation and Pi

import random

n = 10**6
k = 0
s0 = 4

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        k += 1

print((k / n) * s0)

## Decimal!

from decimal import *

s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'

temp = [Decimal(i) for i in s.split()]
print(max(temp) + min(temp))

##

s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'

from decimal import *
temp = [Decimal(i) for i in s.split()]
print(sum(temp))

mx = []
max_d = 0

for i in range(5):
    max_d = max(temp)
    mx.append(max_d)
    temp.remove(max_d)

print(*sorted(mx, reverse = True))

##

from decimal import *
num = abs(Decimal(input()))
num_tuple = num.as_tuple().digits
if num < 1:
    print(max(num_tuple))
else:
    print(max(num_tuple) + min(num_tuple))

##

from decimal import *

d = Decimal(input())

print(d.exp() + d.ln() + d.log10() + d.sqrt())

from fractions import Fraction

numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

resp = [Fraction(i) for i in numbers]

for i in range(len(resp)):
    print(numbers[i], '=', resp[i])

##

from fractions import Fraction

s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'

temp = [Fraction(i) for i in s.split()]
print(Fraction(max(temp)) + Fraction(min(temp)))

##

from fractions import Fraction

m, n = int(input()), int(input())
print(Fraction(m, n))

##

from fractions import Fraction
a, b = input(), input()
a1, b1 = Fraction(a), Fraction(b)

print(a, '+', b, '=', a1 + b1)
print(a, '-', b, '=', a1 - b1)
print(a, '*', b, '=', a1 * b1)
print(a, '/', b, '=', a1 / b1)

## Сумма дробей 1

from fractions import Fraction

n = int(input())
s = Fraction(0)

for i in range(1, n + 1):
    s += Fraction(1, i**2)

print(s)

## Сумма дробей 2

from fractions import Fraction
from math import factorial

n = int(input())
s = Fraction(0)

for i in range(1, n + 1):
    s += Fraction(1, factorial(i))

print(s)

## Упорядоченные дроби

from fractions import Fraction

n = int(input())
resp = set()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j:
            temp = Fraction(i, j)
            resp.add(temp)

for i in sorted(resp):
    print(i)

## Юный математик

from fractions import Fraction

n = int(input())
resp = set()

for i in range(1, n):
    for j in range(1, n):
        if i < j:
            resp.add(Fraction(i, j))

temp = []
for i in resp:
    if i.numerator + i.denominator == n and gcd(i.numerator, i.denominator) == 1:
        temp.append((i))
        
print(max(temp))

## Комплексные числа в Python

z1, z2 = complex(input()), complex(input())

print(f'{z1} + {z2} = {z1 + z2}')
print(f'{z1} - {z2} = {z1 - z2}')
print(f'{z1} * {z2} = {z1 * z2}')

##

numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

temp_list = [abs(i) for i in numbers]
temp_index = temp_list.index(max(temp_list))

print(numbers[temp_index])
print(max(temp_list))

## Сопряженные числа

n = int(input())
z1, z2 = complex(input()), complex(input())

z3, z4 = z1.conjugate(), z2.conjugate()

resp = z1**n + z2**n + z3**n + z4**(n+1)

print(resp)

##

def matrix(n=None, m=None, value=0):
    if n is None:
        n = 1
    if m is None:
        m = n
    
    matrix = [[value] * m for _ in range(n)]
    return matrix

##

def sq_sum(*args):
    result = 0
    for i in range(len(args)):
        result += args[i]**2
    return result

##

from decimal import *

def mean(*args):
    result = 0
    temp = []
    
    for i in range(len(args)):
        if type(args[i]) in (int, float):
            result += Decimal(args[i])
            temp.append(args[i])
            
    if len(temp) == 0:
        return 0.0
    else:
        return result/len(temp)

##

def greet(name, *args):
    if len(args) > 0:
        return(f"Hello, {name} and {' and '.join(args)}!")
    else:
        return(f"Hello, {name}!")

## 

def print_products(*args):
    temp = list()
    
    for i in range(len(args)):
        if type(args[i]) == str and len(args[i]) > 0:
            temp.append(args[i])
            
    if len(temp) == 0:
        return(print('Нет продуктов'))   
    else:
        result = [f"{i+1}) {temp[i]}" for i in range(len(temp))]
        return(print(*result, sep = '\n'))

##

def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f"{k}: {v}")


##

numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
temp = []

for i in range(len(numbers)):
    temp.append(sum(numbers[i])/len(numbers[i]))

print(numbers[temp.index(min(temp))])
print(numbers[temp.index(max(temp))])
## better:
def avg(*args):
    if len(args) == 0:
        return 0
    return sum(*args)/len(*args)

print(min(numbers, key=avg), max(numbers, key=avg), sep='\n') 

##

points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

def where_is_point(point):
    return (point[0]**2 + point[1]**2)**0.5

print(sorted(points, key=where_is_point))

##

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

def sorting(tpl):
    return min(tpl) + max(tpl)

print(sorted(numbers, key=sorting))

## Математические функции

import math

def f1(x):
    return x**2

def f2(x):
    return x**3

def f3(x):
    return x**0.5

def f4(x):
    return abs(x)

def f5(x):
    return math.sin(x)

scope = {
    'квадрат': f1,
    'куб': f2
    'корень': f3,
    'модуль': f4,
    'синус': f5
}

x = int(input())
goal = input()

print(scope[goal](x))

##сортировка-1

def sum_of_numbers(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s

mystr = input().split()
mylst = [int(i) for i in mystr]

print(*sorted(mylst, key=sum_of_numbers))

## сортировка-2

def comparator(num):
    return sum([int(i) for i in str(num)])

numbers = sorted([int(i) for i in input().split()])
print(*sorted(numbers, key=comparator))

##

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def function(num):
    return round(num, 2)

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
temp = map(function, numbers)

print(*temp, sep='\n')

##

def f1(i):
    return 99 < i < 999 and i % 5 == 2

def f2(i):
    return i**3

def map(f2, items):
    result = []
    for item in items:
        result.append(f2(item))
    return result


def filter(f1, items):
    result = []
    for item in items:
        if f1(item):
            result.append(item)
    return result

numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

print(*map(f2, filter(f1, numbers)), sep='\n')

##

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc

def add_sq(i, j):
    return i + j**2

def x_sq(item):
    return item**2

numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

print(reduce(add_sq, numbers, 0))
print(sum(map(x_sq, numbers)))

##

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def x_sq(item):
    return item**2

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def num(item):
    if 9 < abs(item) < 100 and item % 7 == 0:
        return item

numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

new_numbers = filter(num, numbers)

print(sum(map(x_sq, new_numbers)))

##

def func_apply(f, l):
    result = []
    for i in l:
        result.append(f(i))
    return result

##

from functools import reduce 

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)

##

from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

def f(your_list):
    resp = []
    for i in range(len(your_list)):
        if your_list[i][1] >= 10000000 and your_list[i][2] == 'primary':
            resp.append(your_list[i][0])
    return resp

filtered_data = f(data)
result = reduce(lambda x, y: f'{x}, {y}' if x != 'Cities:' else f'{x} {y}', sorted(filtered_data), 'Cities:')
print(result)

##

func = lambda num: num % 13 == 0 or num % 19 == 0
num = int(input())
print(func(num))

##
func = lambda your_lane: your_lane[0] in 'aA' and your_lane[-1] in 'aA'
## or:
func = lambda x: x.lower().startswith('a') and x.lower().endswith('a')

##

is_non_negative_num = lambda your_lane: your_lane.count('.') <= 1 and your_lane.replace('.', '', 1) and your_lane.replace('.', '', 1) and '-' not in your_lane and your_lane.upper() == your_lane.lower()

print(is_non_negative_num('1.23'))

##

is_num = lambda your_lane: your_lane.count('.') <= 1 and your_lane.replace('.', '', 1) and  your_lane.count('-') <= 1 and your_lane.upper() == your_lane.lower() and '-' not in your_lane[1:]

##

words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

print(*sorted(filter(lambda word: len(word) == 6, words)))

##

numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

new1 = list(filter(lambda num: num <= 47 or (num % 2 == 0 and num > 47), numbers))
new2 = list(map(lambda num: num // 2 if num % 2== 0 else num, new1))

print(*new2, sep=' ')

##

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

new_data = sorted(data, key=lambda data: data[1][-1], reverse=True)
for i in range(len(new_data)):
    print(f'{new_data[i][1]}: {new_data[i][0]}')

##
    
data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

new_data = list(sorted(data, key=lambda x: (len(x), x)))
print(*new_data, sep=' ')

##

mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

new_list = list(filter(lambda num: type(num) == int, mixed_list))
print(max(new_list))

##

mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
words = sorted(list(filter(lambda num: type(num) == int, mixed_list)))
nums = sorted(list(filter(lambda num: type(num) == str, mixed_list)))
print(*(words + nums))

## Противоположный цвет

rgb = input().split()
new_color = list(map(lambda value: 255 - int(value), rgb))
print(*new_color)

##

numbers = [10, 30, 20, 50, 40, 60, 70, 80]

total = 0
for index, number in enumerate(numbers, 1):
    if index % 2 == 0:
        total += number
print(total)

##

words1 = ['яблоко', 'ананас', 'апельсин', 'хурма', 'гранат', 'мандарин', 'айва']
words2 = ['林檎', 'パイナップル', 'オレンジ', '柿']
words3 = ['apple', 'pineapple', 'orange', 'persimmon', 'pomegranate']

print(len(list(zip(words1, words2, words3))))

##

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(word in command for word in ignore)

##

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for i, j, k in zip(capitals, countries, population):
    print(f"{i} is the capital of {j}, population equal {k} people.")

## Внутри шара

def is_inside(coordinates, radius):
    return sum(c ** 2 for c in coordinates) <= radius ** 2
          
data = []
for _ in range(3):
    data.append(input().split())

abscissas = [float(x) for x in data[0]]
ordinates = [float(y) for y in data[1]]
applicates = [float(z) for z in data[2]]

rad = 2
coordinates_list = list(zip(abscissas, ordinates, applicates))
all_inside = all(is_inside(coordinates, rad) for coordinates in coordinates_list)

print(all_inside)

## Корректный IP-адрес

def norm_digit(digit):
    return digit.isdigit() and (int(digit) >= 0 and int(digit) <= 255)

print(all(norm_digit(i) for i in (input().split('.'))))

## Interesting number

def is_interesting(num):
    components = []
    temp = 0
    start = num

    while num > 0:
        temp = num % 10
        if temp == 0:
            return False
        components.append(temp)
        num //= 10

    return all(start % i == 0 for i in components)

a, b = int(input()), int(input())
response = list(i for i in range(a, b+1) if is_interesting(i))
print(*response)

## Password

p = input()
if len(p) >= 7:
    if any(c.islower() for c in p) and any(c.isupper() for c in p) and any(c.isdigit() for c in p):
        print('YES')
    else:
        print('NO')
else:
    print('NO') 

## Отличники

data = []

for i in range(int(input())):
    group = []
    for j in range(int(input())):
        group.append(input())
    data.append(group)

resp = [any('5' in j for j in i) for i in data]

if all(resp):
    print('YES')
else:
    print('NO')

## Письмо для экзамена
    
def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return f'''To: {mail}
Приветствую, {name}!
Вам назначен экзамен, который пройдет {date}, в {time}.
По адресу: {place}. 
Экзамен будет проводить {teacher} в кабинете {number}. 
Желаем удачи на экзамене!'''

## Pretty print

def pretty_print(data, side='-', delimiter='|'):
    b = delimiter + ' ' + (' ' + delimiter + ' ').join(map(str, data)) + ' ' + delimiter
    c = ' ' + side*(len(b) - 2) + ' '
    print( f'''{c}
{b}
{c}''')


##
    
def concat(*args, sep=' '):
    return f"{sep}".join(map(str, args))

##

def product_of_odds(data):
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result
#
from functools import reduce

def product_of_odds(data):
    filtered_data = filter(lambda elem: elem % 2 == 1, data)
    result = reduce(lambda x, y:  x * y, filtered_data, 1)
return result

##

words = 'the world is mine take a look what you have started'.split()

print(*map(lambda x: f'"{x}"', words))

##

numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*(str(x) for x in numbers if str(x) != str(x)[::-1]))

##

numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)

print(sorted_numbers)

##

def call(func, *args):
    return func(*args)
def mul7(x):
    return x * 7
def add2(x, y):
    return x + y
def add3(x, y, z):
    return x + y + z

print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))

##

def compose(f, g):
    def composed_functions(x):
        return f(g(x))
    return composed_functions

##

def arithmetic_operation(operation):
    if operation == '+':
        return lambda x, y: x + y
    elif operation == '-':
        return lambda x, y: x - y
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y

##
    
lane = input()
sorted_lane = ' '.join(sorted(lane.split(), key=str.lower))
print(sorted_lane)

##

first_file = open(input())

for line in first_file:
    print(line.strip())

first_file.close()

## Предпоследняя строка

file = open(input())

data_file = file.readlines()
print(data_file[-2].rstrip())

file.close()

## Случайная строка

import random as r
file = open('lines.txt')

data_file = file.readlines()
i = r.randint(0, len(data_file))
print(data_file[i])

file.close()

## Сумма двух-1

file = open('numbers.txt')
data = file.readlines()
print(int(data[0]) + int(data[1]))

file.close()

## Сумма двух-2

file = open('nums.txt')
data = file.read().split()
s = 0
for i in range(len(data)):
    if data[i] != ' ':
        s += int(data[i])

print(s)

file.close()
#better solution:
file = open('nums.txt')

print(sum(map(int, file.read().split())))

file.close()

## Общая стоимость

file = open('prices.txt', 'r', encoding='utf-8')
data = file.readlines()
mylist = []
total = 0
for line in data:
    elements = line.strip().split('\t')
    el_name = elements[0]
    q = int(elements[1])
    price = int(elements[2])
    total_price = q * price
    mylist.append((el_name, q, price, total_price))

s = 0
for i in mylist:
    s += int(i[-1])

print(s)

## Переворот строки

with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[::-1])

## Обратный порядок

with open('data.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines()[::-1]:
        print(i.strip())

## Длинные строки

with open('lines.txt') as f:
    temp = f.readlines()
    temp = [i.strip() for i in temp]
    m = max(len(i) for i in temp)
    for i in temp:
        if len(i) == m:
            print(i)

## Сумма чисел в строках

with open('numbers.txt') as n:
    resp = [sum(map(int, i.split())) for i in n.readlines()]
    print(*resp, sep='\n')

## Сумма чисел в файле, замена символов в строке

with open('nums.txt') as n:
    old = n.read()
    new = ''.join(char if char.isdigit() else ' ' for char in old).split()
    print(sum(map(int, new)))

## Статистика по файлу

with open('file.txt') as data:
    lines = data.readlines()
    words = sum(len(i.strip().split()) for i in lines)
    letters = []
    for i in lines:
        for j in range(len(i)):
            if i[j].isalpha():
                letters += i[j]
    
    print(f'''Input file contains:
    {len(letters)} letters
    {words} words
    {len(lines)} lines''')

## Random name and surname
    
import random as r
with open('first_names.txt') as fn, open('last_names.txt') as ln:
    first = fn.readlines()
    last = ln.readlines()
    for i in range(3):
        print(f'''{r.choice(first).strip()} {r.choise(last).strip()}''')

## Необычные страны

with open('population.txt') as f:
    file = f.readlines()
    for line in file:
        parts = line.strip().split('\t')
        if parts[0].startswith('G') and int(parts[1]) > 500000:
            print(parts[0])

## CSV
            
def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        data_lines = lines[1:]
        result = []
        for line in data_lines:
            values = line.strip().split(',')
            temp = {headers[i]: values[i] for i in range(len(headers))}
            result.append(temp)
    return result                

## Входная строка

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(input())

## Случайные числа
   
import random as r

with open('random.txt', 'w', encoding='utf-8') as f:
    print(*[r.randint(111, 777) for i in range(25)], sep='\n', file=f)

## Нумерация строк

with open('input.txt', 'r', encoding='utf-8') as i, open('output.txt', 'w', encoding='utf-8') as o:
    inp = i.readlines()

    for lane in enumerate(inp, 1):
        o.write(f"{lane[0]}) {lane[1]}")

## Подарок 
        
with open('class_scores.txt', 'r') as i, open('new_scores.txt', 'w') as o:
    inp = i.readlines()

    for lane in inp:
        parts = lane.split()
        name = parts[0]
        score = int(parts[1])
        mrk = score + 5
        new_s = min(100, mrk)
        o.write(f"{name} {new_s}\n")