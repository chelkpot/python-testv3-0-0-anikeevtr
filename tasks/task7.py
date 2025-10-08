# tasks/task7.py

def solve():
# Ниже пишите решение задачи
    # Задача 2: Шифр данных
    x = int(input())
    
    # Получаем цифры числа
    chislo1 = x // 1000  # первая цифра
    chislo2 = (x // 100) % 10  # вторая цифра
    chislo3 = (x // 10) % 10   # третья цифра
    chislo4 = x % 10           # четвертая цифра
    
    # Заменяем каждую цифру значением (цифра + 7) % 10
    new_chislo1 = (chislo1 + 7) % 10
    new_chislo2 = (chislo2 + 7) % 10
    new_chislo3 = (chislo3 + 7) % 10
    new_chislo4 = (chislo4 + 7) % 10
    
    # Меняем местами: первая с третьей, вторая с четвертой
    encrypted = new_chislo3 * 1000 + new_chislo4 * 100 + new_chislo1 * 10 + new_chislo2
    
    print(encrypted)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()
