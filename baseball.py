# from random import randint
#
#
# def generate_numbers():
#     numbers = []
#     while len(numbers) < 3:
#         num = randint(0, 9)
#         if num not in numbers:
#             numbers.append(num)
#
#     # 코드를 작성하세요.
#
#     print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
#     return numbers
#
#
# print(generate_numbers())


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1

    for i in range(3):
        if guess[i] in solution and guess[i] != solution[i]:
            ball_count += 1

    return strike_count, ball_count


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    count = 1
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        num = input("{}번째 숫자를 입력하세요: ".format(count))
        if num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif int(num) > 9 or 0 > int(num):
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)
            count += 1


    return new_guess


guse = []
guse = take_guess()
print(guse)

#
# from random import randint
#
#
# def generate_numbers():
#     # 지난 과제의 코드를 붙여 넣으세요.
#
#
# def take_guess():
#     # 지난 과제의 코드를 붙여 넣으세요.
#
#
# def get_score(guess, solution):
#     # 지난 과제의 코드를 붙여 넣으세요.
#
#
# # 여기서부터 게임 시작!
# ANSWER = generate_numbers()
# tries = 0
#
# # 코드를 작성하세요.
#
# print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
