x = 9 ** 1700 + 3 ** 1800 - 3 ** 350 + 2
k = 0
while x > 0:
    if x % 3 == 2:
        k += 1
    x = x // 3
print(k)
