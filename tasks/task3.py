# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    
    # Номиналы купюр: 100, 20, 10, 5, 1 (в порядке убывания)
    # Использую "жадный" алгоритм для минимального количества купюр
    
    count_sotok = n // 100
    n = n % 100
    
    count_dvadcat = n // 20
    n = n % 20
    
    count_desyatok = n // 10
    n = n % 10
    
    count_pyatok = n // 5
    n = n % 5
    
    count_odinok = n
    
    total_bills = count_sotok + count_dvadcat + count_desyatok + count_pyatok + count_odinok
    print(total_bills)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()