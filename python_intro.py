r"""
Приклади з розділу «Вступ до Python» посібника Django Girls.
Запуск: myvenv\Scripts\python.exe python_intro.py
"""


def main() -> None:
    # 1. Арифметичні операції
    print("=== 1. Арифметика ===")
    print("2 + 3 =", 2 + 3)
    print("4 * 5 =", 4 * 5)
    print("5 - 1 =", 5 - 1)
    print("40 / 2 =", 40 / 2)
    print("2 ** 3 =", 2 ** 3)

    # 2. Рядки (Strings)
    print("\n=== 2. Рядки ===")
    print("Hi there " + "Ola")
    print("Ola" * 3)
    print("Ola".upper())
    print("Довжина 'Ola':", len("Ola"))
    print("Довжина str(304023):", len(str(304023)))

    # 3. Змінні (Variables)
    print("\n=== 3. Змінні ===")
    name = "Ola"
    print("name =", name)
    name = "Sonja"
    print("Нове значення name =", name, "| довжина:", len(name))
    a = 4
    b = 6
    print("a * b =", a * b)

    # 4. Списки (Lists)
    print("\n=== 4. Списки ===")
    lottery = [3, 42, 12, 19, 30, 59]
    print("Початковий список lottery:", lottery)
    print("Довжина списку:", len(lottery))
    lottery.sort()
    print("Після sort():", lottery)
    lottery.reverse()
    print("Після reverse():", lottery)
    lottery.append(199)
    print("Після append(199):", lottery)
    print("Перший елемент lottery[0]:", lottery[0])
    print("Другий елемент lottery[1]:", lottery[1])
    removed = lottery.pop(0)
    print(f"Після pop(0) (видалено {removed}):", lottery)

    # 5. Словники (Dictionaries)
    print("\n=== 5. Словники ===")
    participant = {
        "name": "Ola",
        "country": "Poland",
        "favorite_numbers": [7, 42, 92],
    }
    print("Учасник:", participant)
    print("Ім'я:", participant["name"])
    participant["favorite_language"] = "Python"
    print("Кількість ключів після додавання favorite_language:", len(participant))
    participant.pop("favorite_numbers")
    participant["country"] = "Ukraine"
    print("Оновлений словник:", participant)

    # 6. Порівняння та логічні операції (Booleans)
    print("\n=== 6. Порівняння та логіка ===")
    print("5 > 2:", 5 > 2)
    print("3 < 1:", 3 < 1)
    print("5 > 2 * 2:", 5 > 2 * 2)
    print("1 == 1:", 1 == 1)
    print("5 != 2:", 5 != 2)
    print("6 >= 12 / 2:", 6 >= 12 / 2)
    print("3 <= 2:", 3 <= 2)
    print("6 > 2 and 2 < 3:", 6 > 2 and 2 < 3)
    print("3 > 2 and 2 < 1:", 3 > 2 and 2 < 1)
    print("3 > 2 or 2 < 1:", 3 > 2 or 2 < 1)

    # 7. Умовні конструкції if ... elif ... else
    print("\n=== 7. Умовні конструкції (if / elif / else) ===")
    if 3 > 2:
        print("It works!")

    if 5 > 2:
        print("5 is indeed greater than 2")
    else:
        print("5 is not greater than 2")

    user_name = "Sonja"
    if user_name == "Ola":
        print("Hey Ola!")
    elif user_name == "Sonja":
        print("Hey Sonja!")
    else:
        print("Hey anonymous!")

    # Приклад із гучністю (volume)
    volume = 57
    if volume < 20:
        print("It's kinda quiet.")
    elif 20 <= volume < 40:
        print("It's nice for background music")
    elif 40 <= volume < 60:
        print("Perfect, I can hear all the details")
    elif 60 <= volume < 80:
        print("Nice for parties")
    elif 80 <= volume < 100:
        print("A bit loud!")
    else:
        print("My ears are hurting! :(")

    # Змінити гучність, якщо вона занадто тиха або занадто голосна
    if volume < 20 or volume > 80:
        volume = 50
        print("That's better!")

    # 8. Власні функції (Functions)
    print("\n=== 8. Функції ===")

    def hi_greeting(person: str) -> None:
        if person == "Ola":
            print("Hi Ola!")
        elif person == "Sonja":
            print("Hi Sonja!")
        else:
            print("Hi anonymous!")

    hi_greeting("Ola")
    hi_greeting("Sonja")
    hi_greeting("Denis")

    # 9. Цикли (Loops)
    print("\n=== 9. Цикли for ===")

    def hi(girl_name: str) -> None:
        print("Hi " + girl_name + "!")

    girls = ["Rachel", "Monica", "Phoebe", "Ola", "You"]
    for girl in girls:
        hi(girl)
        print("Next girl")

    print("\nЦикл із range(1, 6):")
    for i in range(1, 6):
        print(i)


if __name__ == "__main__":
    main()
