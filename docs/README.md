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
