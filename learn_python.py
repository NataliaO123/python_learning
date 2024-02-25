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
