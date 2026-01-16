import math

def calculate_perimeter(a, b, h):
    d = (a - b) / 2  # Половина разности оснований
    c = math.sqrt(h**2 + d**2)  # Длина боковой стороны
    return a + b + 2 * c  # Периметр

# Пример использования
if __name__ == "__main__":
    try:
        a = float(input("Введите длину нижнего основания (a): "))
        b = float(input("Введите длину верхнего основания (b): "))
        h = float(input("Введите высоту (h): "))
        
        if a <= 0 or b <= 0 or h <= 0:
            print("Длины оснований и высота должны быть положительными числами.")
        else:
            perimeter = calculate_perimeter(a, b, h)
            print(f"Периметр равнобедренной трапеции: {perimeter:.2f}")
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")




