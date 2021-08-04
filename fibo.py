def fibona(n):
    if n == 1 or n == 2:
        return 1
    return fibona(n - 1) + fibona(n - 2)

for i in range(1, 11):
    print(fibona(i))