def calculate_cube_properties(edge_length):
    """Вычисляет объем и площадь боковой поверхности куба."""
    volume = edge_length ** 3
    lateral_surface_area = 4 * edge_length ** 2
    return volume, lateral_surface_area

if __name__ == "__main__":
    # Ввод длины ребра куба
    edge_length = float(input("Введите длину ребра куба: "))
    
    # Вычисление объема и площади боковой поверхности
    volume, lateral_surface_area = calculate_cube_properties(edge_length)
    
    # Вывод результата
    print(f"Объем куба: {volume:.2f}")
    print(f"Площадь боковой поверхности куба: {lateral_surface_area:.2f}")
