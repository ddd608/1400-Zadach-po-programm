import math

def calculate_perimeter(a, b):
    c = math.sqrt(a**2 + b**2)  # Вычисляем гипотенузу
    return a + b + c  # Возвращаем периметр

# Пример использования
if __name__ == "__main__":
    try:
        a = float(input("Введите длину первого катета (a): "))
        b = float(input("Введите длину второго катета (b): "))
        
        if a <= 0 or b <= 0:
            print("Длины катетов должны быть положительными числами.")
        else:
            perimeter = calculate_perimeter(a, b)
            print(f"Периметр прямоугольного треугольника: {perimeter:.2f}")
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")



