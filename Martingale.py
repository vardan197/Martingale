import random

HEADS = "heads"
TAILS = "tails"

COIN_VALUES = [HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUES)


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet
    max_win = 0   # Переменная для отслеживания максимального выигрыша

    while current_funds > 0:
        print("----------")
        steps_to_loose += 1
        current_funds -= current_bet
        print(f"{current_funds=}, {current_bet=}")

        flipped_coin_value = flip_coin()
        if flipped_coin_value == HEADS:
            win = current_bet * 2
            print(f"{win=}")
            current_funds += win
            max_win = max(max_win, win)  # Обновление максимального выигрыша
            current_bet = min_bet




        else:
            print("loose")
            current_bet *=2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds

    return steps_to_loose, max_win  # Возвращаем также максимальный выигрыш

# Вызов функции и вывод результата
steps, max_win = play_martingale(starting_funds=100, min_bet=1, max_bet=100)
print(f"Total steps to lose: {steps}, Max win: {max_win}")