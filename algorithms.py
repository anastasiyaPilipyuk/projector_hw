def put_on_hat(count: int, iteration: int) -> list:
    arr_cats = [False for _ in range(count)]
    i = 0
    while i < iteration:
        j = i
        step = j + 1
        while j < len(arr_cats):
            arr_cats[j] = not arr_cats[j]
            j += step
        i += 1
    return [index+1 for index, value in enumerate(arr_cats) if value]


print(put_on_hat(100, 100))
