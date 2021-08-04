# with open('vocabulary.txt', 'a') as f:
#     while True:
#         eng = input("영어 단어를 입력하세요:")
#         if eng == 'q':
#             break
#         kor = input("한국어 뜻을 입력하세요:")
#         f.write("{}: {}\n".format(eng, kor))

# with open('vocabulary.txt', 'r') as f:
#     for line in f:
#         data = line.strip().split(": ")
#         english_word, korean_word = data[0], data[1]
#
#         # 유저 입력값 받기
#         guess = input("{}: ".format(korean_word))
#
#         # 정답 확인하기
#         if guess == english_word:
#             print("정답입니다!\n")
#         else:
#             print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))


import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]

    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))

    # 프로그램 끝내기
    if guess == 'q':
        break

    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))