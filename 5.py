for n in range(200, 1, -1):
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    r = int(b, 2)
    if r <= 57:
        print(r)
        break
        