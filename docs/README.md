#Общее описание решения 
Проект geometric_lib - это библиотека на языке Python, предназначенная для работы с геометрическими фигурами. Она предоставляет функциональность для вычисления периметра и площади различных фигур, таких как круг и квадрат. 
 
Библиотека состоит из нескольких модулей, каждый из которых отвечает за определенную фигуру. Например, модуль circle содержит функции для вычисления периметра и площади круга, а модуль square - для квадрата. Каждый модуль экспортирует соответствующие функции, которые могут быть использованы другими частями программы. 
 
 
# How to use calculator: 
1. Run python calculate.py 
2. Enter the figure name. Available are Circle, Square. 
3. Enter the function: Area or Perimeter. 
4. Enter figure sizes. Radius for circle, one side for square. 
5. Get the answer! 
 
# Math formulas 
## Area 
- Circle: S = πR² 
- Rectangle: S = ab 
- Square: S = a² 
- Triangle: S = sqrt(p * (p-a) * (p-b) * (p-c)) where p is semiperimeter 
 
## Perimeter 
- Circle: P = 2πR 
- Rectangle: P = 2a + 2b 
- Square: P = 4a 
- Triangle: P = a + b + c 
 
#Описание каждой функции с примерами вызова 
 
##Circle 
 
area: 
Возвращает значение площади круга с заданным радиусом 
a = 4 
area(a) = 50.26548245743669 
 
perimeter 
Возвращает значение периметра круга с заданным радиусом 
a = 4 
perimeter(a) = 25.132741228718345 

##Square 
 
area: 
Возвращает значение площади квадрата с заданной стороной 
a = 4 
area(a) = 16 
 
perimeter: 
Возвращает значение периметра квадрата с заданной стороной 
a = 4 
perimeter(a) = 16 
 
##Triangle 
 
area: 
Возвращает полупериметр треугольника с заданными сторонами 
a, b, c = 3, 4, 5 
area(a, b, c) = 6.0 
 
perimeter: 
Возвращает значение периметра треугольника с заданными сторонами 
a, b, c = 3, 4, 5 
perimeter(a, b, c) = 12 
 
##Calculate 
Ничего не возвращает


#Изменения с хешами коммитов

commit 08e6e9e43c174f34af0661ce699b5afa313ff91d
Author: Olga <gusinao652@gmail.com>
Date:   Tue Oct 1 19:01:05 2024 +0300

    Добавлены изменения в файлы

commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
