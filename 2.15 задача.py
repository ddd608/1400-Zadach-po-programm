import math

def calculate_ring_area(R, r):
    return math.pi * (R**2 - r**2)

# Пример использования
if __name__ == "__main__":
    try:
        R = float(input("Введите внешний радиус (R): "))
        r = float(input("Введите внутренний радиус (r): "))
        
        if R <= r:
            print("Внешний радиус должен быть больше внутреннего радиуса.")
        else:
            area = calculate_ring_area(R, r)
            print(f"Площадь кольца: {area:.2f}")
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения.")
