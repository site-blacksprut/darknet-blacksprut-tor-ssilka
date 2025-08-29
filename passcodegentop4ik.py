# password_generator.py
import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """
    Генерирует случайный пароль.
    
    :param length: Длина пароля
    :param use_uppercase: Использовать заглавные буквы
    :param use_digits: Использовать цифры
    :param use_symbols: Использовать спецсимволы
    :return: Сгенерированный пароль
    """
    # Начинаем с маленьких букв (обязательная база)
    chars = string.ascii_lowercase
    
    # Добавляем другие символы по желанию
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Генерируем пароль
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("🔐 Генератор случайных паролей")
    print("—" * 40)
    print("Настрой параметры или оставь по умолчанию.")

    try:
        length = int(input("🔹 Длина пароля (по умолчанию 12): ") or "12")
        if length < 4:
            print("⚠️  Слишком короткий пароль! Установлено 8.")
            length = 8

        use_uppercase = input("🔹 Использовать заглавные буквы? (Д/н, по умолчанию Д): ").strip().lower() != "н"
        use_digits = input("🔹 Использовать цифры? (Д/н, по умолчанию Д): ").strip().lower() != "н"
        use_symbols = input("🔹 Использовать символы? (Д/н, по умолчанию Д): ").strip().lower() != "н"

        # Генерация
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        
        print("\n" + "✅ Сгенерированный пароль:")
        print("🔐 " + password)
        print("\n💡 Совет: Не используй его на важных сайтах без проверки.")
        
    except KeyboardInterrupt:
        print("\n\n👋 Пока! Выход по Ctrl+C.")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")

if __name__ == "__main__":
    main()
