from random import randint


def generate_numbers(n):
    # 지난 과제의 코드를 붙여 넣으세요.
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    numbers.sort()
    return numbers


def draw_winning_numbers():
    # 코드를 작성하세요.
    win_num = generate_numbers(6)
    while len(win_num) < 7:
        num = randint(1, 45)
        if num not in win_num:
            win_num.append(num)
    return win_num


def count_matching_numbers(list_1, list_2):
    # 코드를 작성하세요.
    same = list(set(list_1).intersection(list_2))
    return len(same)


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    same = count_matching_numbers(numbers, winning_numbers[:6])
    if same == 6:
        return 1000000000
    elif same == 5:
        bonus = count_matching_numbers(numbers, winning_numbers[6:])
        if same + bonus == 6:
            return 50000000
        else:
            return 1000000
    elif same == 4:
        return 50000
    elif same == 3:
        return 5000
    else:
        return 0


# 예시 결과 출력
print(draw_winning_numbers())
