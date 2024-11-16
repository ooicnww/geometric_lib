import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
    "perimeter-square": 1
}

def calc(fig, func, size):
    assert fig in figs, f"Invalid figure: {fig}. Available options: {figs}"
    assert func in funcs, f"Invalid function: {func}. Available options: {funcs}"

    modules = {"circle": circle, "square": square}
    result = getattr(modules[fig], func)(*size)
    return f'{func} of {fig} is {result}'

if __name__ == "__main__":
    try:
        func = ''
        fig = ''
        size = list()

        while fig not in figs:
            fig = input(f"Enter figure name, available are {figs}:\n")

        while func not in funcs:
            func = input(f"Enter function name, available are {funcs}:\n")

        while len(size) != sizes.get(f"{func}-{fig}", 1):
            try:
                size = list(map(int, input(
                    "Input figure sizes separated by space, 1 for circle and square\n").split()))
            except ValueError:
                print("Invalid input. Please enter integers.")

        print(calc(fig, func, size))
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
