import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# Пример использования
if __name__ == "__main__":
    try:
        a = float(input("Введите длину первого катета (a): "))
        b = float(input("Введите длину второго катета (b): "))
        
        hypotenuse = calculate_hypotenuse(a, b)
        print(f"Длина гипотенузы: {hypotenuse}")
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")
