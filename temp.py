'''
# Тестовые данные.
TEST_DATA: list[tuple[int, str, bool]] = [
    (43, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(
        current_rep: float, rep_points: int, debuf_effect: bool) -> float:
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res: list[tuple[int, str, bool]]) -> str:
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (
        f'После {len(duel_res)} поединков,'
        f' репутация персонажа — {current_rep:.3f} очков.')


# Тестовый вызов функции main.
print(main(TEST_DATA))
'''
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления'
           ' квадратного корня из заданного числа')

print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет и выводит результат."""
    if your_number >= 0:
        res = calculate_square_root(your_number)
        print(f'Мы вычислили квадратный корень из '
              f'введённого вами числа. Это будет: {res}')


calc(25.5)
