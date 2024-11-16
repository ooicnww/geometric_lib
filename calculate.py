import circle  # noqa: F401
import square  # noqa: F401

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs
    result = eval(f'{fig}.{func}(*{size})')
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
            size_input = input(
                "Input figure sizes separated by space, 1 for circle and square\n"
            )
            size = list(map(int, size_input.split()))

        print(calc(fig, func, size))
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
