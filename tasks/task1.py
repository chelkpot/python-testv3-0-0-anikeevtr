# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    
    # Получаем разряды числа
    sotki = n // 100
    desyatki = (n // 10) % 10
    odni = n % 10
    
    # Вычисляем сумму разрядов
    sum_digits = sotki + desyatki + odni
    
    print(sum_digits)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()