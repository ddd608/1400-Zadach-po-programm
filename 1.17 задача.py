def calculate_function_y1(x):
    """Вычисляет значение функции y = 17x^2 - 6x + 13"""
    y = 17 * (x ** 2) - 6 * x + 13
    return y

def calculate_function_y2(a):
    """Вычисляет значение функции y = 3a^2 + 5a - 21"""
    y = 3 * (a ** 2) + 5 * a - 21
    return y
if __name__ == "__main__":
    # Ввод значения x для первой функции
    x_value = float(input("Введите значение x для функции y = 17x^2 - 6x + 13: "))
    result_y1 = calculate_function_y1(x_value)
    print(f"Значение функции y = 17x^2 - 6x + 13 при x = {x_value}: {result_y1}")

    # Ввод значения a для второй функции
    a_value = float(input("Введите значение a для функции y = 3a^2 + 5a - 21: "))
    result_y2 = calculate_function_y2(a_value)
    print(f"Значение функции y = 3a^2 + 5a - 21 при a = {a_value}: {result_y2}")
