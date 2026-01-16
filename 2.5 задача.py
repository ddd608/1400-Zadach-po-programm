def calculate_diameter(radius):
    """Вычисляет диаметр окружности по радиусу."""
    diameter = 2 * radius
    return diameter

if __name__ == "__main__":
    # Ввод радиуса окружности
    radius = float(input("Введите радиус окружности: "))
    
    # Вычисление диаметра
    diameter = calculate_diameter(radius)
    
    # Вывод результата
    print(f"Диаметр окружности с радиусом {radius} равен: {diameter}")
