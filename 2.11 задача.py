def calculate_density(mass, volume):
    """Вычисляет плотность материала."""
    if volume == 0:  # Проверка на ноль, чтобы избежать деления на ноль
        raise ValueError("Объем не может быть равен нулю.")
    return mass / volume

if __name__ == "__main__":
    try:
        # Ввод массы и объема
        mass = float(input("Введите массу тела (в кг): "))
        volume = float(input("Введите объем тела (в м³): "))
        
        # Вычисление плотности
        density = calculate_density(mass, volume)
        
        # Вывод результата
        print(f"Плотность материала: {density} кг/м³")
    except ValueError as e:
        print(f"Ошибка: {e}")
