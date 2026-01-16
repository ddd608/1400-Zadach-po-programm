import math

def calculate_circle_properties(radius):
    """Вычисляет длину окружности и площадь круга."""
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

if __name__ == "__main__":
    # Ввод радиуса окружности
    radius = float(input("Введите радиус окружности: "))
    
    # Вычисление длины окружности и площади круга
    circumference, area = calculate_circle_properties(radius)
    
    # Вывод результата
    print(f"Длина окружности: {circumference:.2f}")
    print(f"Площадь круга: {area:.2f}")
