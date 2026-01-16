def calculate_x(a, b):
    """Вычисляет значение функции x = 3.14(a + b)^3 + 2.75b^2 - 12.7a - 4.1."""
    result = 3.14 * ((a + b) ** 3) + 2.75 * (b ** 2) - 12.7 * a - 4.1
    return result

if __name__ == "__main__":
    # Ввод значений a и b
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    
    # Вычисление значения функции x
    result = calculate_x(a, b)
    
    # Вывод результата
    print(f"Значение функции x при a = {a} и b = {b}: {result:.2f}")
