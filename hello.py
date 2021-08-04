import random

# 코드를 작성하세요.
answer = random.randint(1, 20)
count = 4

while count > 0:
    guess = int(input("기회가 {}번 남았습니다. 1-20사이의 숫자를 맞혀보세요: ".format(count)))
    if answer < guess:
        print("Down")
        count -= 1
    elif answer > guess:
        print("Up")
        count -= 1
    else:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(5 - count))
        break
    if count == 0:
        print("아쉽습니다. 정답은 {}입니다.".format(answer))
