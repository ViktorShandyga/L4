#1
age = int(input("Введіть ваш вік: "))

if age >= 18:

   print("Ви можете зайти на сайт!")
if age < 18:

   print("Ви не можете зайти на сайт!")

#2
import random


def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    print("Вітаю! Я загадую число від 1 до 10. Спробуйте вгадати його.")

    while True:
        user_input = input("Введіть ваше число: ")

        if not user_input.isdigit():
            print("Будь ласка, введіть ціле число.")
            continue

        user_guess = int(user_input)
        attempts += 1

        if user_guess < number_to_guess:
            print("Загадане число більше.")
        elif user_guess > number_to_guess:
            print("Загадане число менше.")
        else:
            print(f"Вітаю! Ви вгадали число {number_to_guess} з {attempts} спроб.")
            break


if __name__ == "__main__":
    guess_the_number()
#3
def calculate_factorial(x):

   result = 1

   for i in range(1, x + 1):

       result *= i

   return result

n = int(input('Введіть число: '))

print(f'Факторіал {n}! = {calculate_factorial(n)}')