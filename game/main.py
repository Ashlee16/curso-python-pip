import random

def choose_options():
    options = ("Piedra", "Papel", "Tijera")
    user_option = input("Piedra, Papel o Tijera: ")
    user_option = user_option.lower()

    if not user_option in options:
        print("La opción no es válida")
        # Continue
        return None, None

    computer_option = random.choice(options)

    print("User option: ", user_option)
    print("Computer option: ", computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("¡Empate!")
    elif user_option == "Piedra":
        if computer_option == "Tijera":
            print("¡User ganó!")
            user_wins += 1
        else:
            print("¡Computer ganó!")
            computer_wins += 1
    elif user_option == "Papel":
        if computer_option == "Piedra":
            print("¡User ganó!")
            user_wins += 1
        else:
            print("¡Computer ganó!")
            computer_wins += 1
    elif user_option == "Tijera":
        if computer_option == "Papel":
            print("¡User ganó!")
            user_wins += 1
        else:
            print("¡Computer ganó!")
            computer_wins += 1
    return user_wins, computer_option


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print("Computer ganó", computer_wins)
        print("User ganó", user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('El ganador es la computadora')
            break

        if user_wins == 2:
            print('El ganador es el usuario')
            break


run_game()
