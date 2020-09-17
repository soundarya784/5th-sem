def rod_cut(price, n):
    i = 0
    max_val = -1
    if n == 0:
        return 0
    while i < n:

        if values[n - 1] != -1: #check if n value already exists
            return values[n - 1]
        max_val = max(max_val, price[i] + rod_cut(price, n - i - 1))
        i += 1
    values[i - 1] = max_val
    return values[i - 1]


price = [1, 5, 8, 9, 10, 17, 17, 20]
length = [1, 2, 3, 4, 5, 6, 7, 8]
values = [-1] * 5
print(rod_cut(price, 5))
