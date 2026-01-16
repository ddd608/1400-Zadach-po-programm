def calculate_population_density(population, area):
    """Вычисляет плотность населения."""
    if area == 0:  # Проверка на ноль, чтобы избежать деления на ноль
        raise ValueError("Площадь территории не может быть равна нулю.")
    return population / area

if __name__ == "__main__":
    try:
        # Ввод количества жителей и площади территории
        population = int(input("Введите количество жителей: "))
        area = float(input("Введите площадь территории (в км²): "))
        
        # Вычисление плотности населения
        population_density = calculate_population_density(population, area)
        
        # Вывод результата
        print(f"Плотность населения: {population_density:.2f} чел/км²")
    except ValueError as e:
        print(f"Ошибка: {e}")
