def sum_digits(n):
    num = str(n)
    if len(num) == 1:
        return int(n)

    return int(num[0]) + sum_digits(int(num[1:]))


print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))