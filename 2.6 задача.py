import math

def calculate_distance_to_horizon(radius, height):
    """Вычисляет расстояние до линии горизонта."""
    distance = math.sqrt(2 * radius * height + height**2)
    return distance

if __name__ == "__main__":
    # Радиус Земли в километрах
    R = 6350
    
    # Ввод высоты над уровнем моря в километрах
    height = float(input("Введите высоту над уровнем моря (в км): "))
    
    # Вычисление расстояния до линии горизонта
    distance = calculate_distance_to_horizon(R, height)
    
    # Вывод результата
    print(f"Расстояние до линии горизонта с высоты {height} км составляет: {distance:.2f} км")
