import math

def calculate_arithmetic_mean(a, b):
    """Вычисляет среднее арифметическое двух чисел."""
    return (a + b) / 2

def calculate_geometric_mean(a, b):
    """Вычисляет среднее геометрическое двух чисел."""
    return math.sqrt(a * b)

if __name__ == "__main__":
    # Ввод двух целых чисел
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))
    
    # Вычисление средних значений
    arithmetic_mean = calculate_arithmetic_mean(a, b)
    geometric_mean = calculate_geometric_mean(a, b)
    
    # Вывод результатов
    print(f"Среднее арифметическое: {arithmetic_mean}")
    print(f"Среднее геометрическое: {geometric_mean}")
