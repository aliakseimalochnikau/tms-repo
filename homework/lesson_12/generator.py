def generate_squares(count):
    for num in range(1, count + 1):
        yield num ** 2


for i in generate_squares(10):
    print(i)

    