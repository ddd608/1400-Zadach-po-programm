def calculate_perimeter(side_length):
    """Вычисляет периметр квадрата по длине его стороны."""
    perimeter = 4 * side_length
    return perimeter

if __name__ == "__main__":
    # Ввод длины стороны квадрата
    side_length = float(input("Введите длину стороны квадрата: "))
    
    # Вычисление периметра
    perimeter = calculate_perimeter(side_length)
    
    # Вывод результата
    print(f"Периметр квадрата со стороной {side_length} равен: {perimeter}")

