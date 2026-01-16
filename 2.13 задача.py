def solve_linear_equation(a, b):
    if a == 0:
        raise ValueError("Коэффициент a не может быть равен нулю.")
    
    # Находим x
    x = -b / a
    return x

# Пример использования
if __name__ == "__main__":
    try:
        a = float(input("Введите коэффициент a (a ≠ 0): "))
        b = float(input("Введите коэффициент b: "))
        
        solution = solve_linear_equation(a, b)
        print(f"Решение уравнения {a}x + {b} = 0: x = {solution}")
    except ValueError as e:
        print(e)
