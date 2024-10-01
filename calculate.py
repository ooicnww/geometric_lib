
import circle  # Импорт модуля circle
import square  # Импорт модуля square
figs = ['circle', 'square']  # Список доступных фигур
funcs = ['perimeter', 'area']  # Список доступных функций
sizes = {}  # Словарь для хранения размеров фигур
def calc(fig, func, size):
    """
    Вычисляет периметр или площадь заданной фигуры.
    Параметры:
    - fig (str): название фигуры ('circle' или 'square')
    - func (str): название функции ('perimeter' или 'area')
    - size (list): список размеров фигуры
    Возвращает:
    - None
    """
    assert fig in figs  # Проверка, что фигура находится в списке доступных фигур
    assert func in funcs  # Проверка, что функция находится в списке доступных функций
    result = eval(f'{fig}.{func}(*{size})')  # Вычисление периметра или площади фигуры
    print(f'{func} of {fig} is {result}')  # Вывод результата
if name == "__main__":
    func = ''  # Инициализация переменной для хранения названия функции
    fig = ''  # Инициализация переменной для хранения названия фигуры
    size = list()  # Инициализация списка для хранения размеров фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")  # Запрос названия фигуры у пользователя
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")  # Запрос названия функции у пользователя
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))  # Запрос размеров фигуры у пользователя
    calc(fig, func, size)  # Вызов функции calc с введенными параметрами
