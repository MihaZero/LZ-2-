import random

def guess_number_game():
    # Компьютер загадывает число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Привет! Я загадал число от 1 до 100. Попробуй угадать!")
    
    while True:
        try:
            # Просим пользователя ввести число
            user_guess = int(input("Введите ваше число: "))
            attempts += 1
            
            # Проверяем условия
            if user_guess < secret_number:
                print("Загаданное число БОЛЬШЕ.")
            elif user_guess > secret_number:
                print("Загаданное число МЕНЬШЕ.")
            else:
                print(f"Поздравляю! Вы угадали число за {attempts} попыток!")
                break # Выходим из цикла, игра окончена
                
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

# Запуск игры
if __name__ == "__main__":
    guess_number_game()

