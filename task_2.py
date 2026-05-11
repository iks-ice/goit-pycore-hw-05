import re
from typing import Callable


def generator_numbers(text: str):
    pattern = re.compile(r"\s([0-9.,]+)\s")
    pos = 0
    while True:
        number = pattern.search(text, pos)
        if number:
            yield number.group().strip()
            pos = number.span()[1]
        else:
            break

def total_profit(text: str, func: Callable):
    return sum([float(x) for x in func(text)])

t = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

res = total_profit(t, generator_numbers)

print(res)
