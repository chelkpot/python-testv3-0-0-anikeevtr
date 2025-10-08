# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    
    # Учитываем только минуты текущих суток (1440 минут = 24 часа)
    n = n % 1440
    
    # Вычисляем часы и минуты
    hours = n // 60
    minutes = n % 60
    
    print(hours, minutes)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()