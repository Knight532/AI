from colorama import Fore
import random


answers = ["Привіт", "Вітаю", "Hello"]

print(f"\n{Fore.CYAN}Chat\n{Fore.RESET}")

while True:
    user_input = input(f"{Fore.YELLOW}Введіть запит: {Fore.RESET}")
    if user_input.lower() == "привіт":
        chat_answers = random.choice(answers)
        print(chat_answers)

    if user_input.lower() == "exit":
        break