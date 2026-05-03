import random

LEVELS = ('Easy', 'Medium', 'Hard')
CHANCES = {'Easy': 10, 'Medium': 5, 'Hard': 3}

def menu():
    print()
    print("="*50)
    print("Welcome to the Number Guessing Game!")
    print("="*50)
    print('\n')
    print("Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)\n0. Quit")
    print('\n')

def guess(nb_chances:int) -> str:
    

    nombre = random.randint(1,10)

    attempts = 0

    while True:

        try :
            guess = int(input('Enter your guess : '))
        except ValueError :
            print("Please enter a valid number !")
            continue
        
        if guess == 0:
            return 'n'

        attempts += 1
        nb_chances -= 1   

        if nombre == guess :
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print("="*50)
            return input('Replay (Y or N) : ').lower()
            
        hint = "less" if nombre < guess else "greater"
        print(f'Incorrect! Please retry, The number is {hint} than {guess}')
        
        
        if nb_chances == 0:
            print(f"You're out of chances ! The number was {nombre}.")
            print("="*50)
            return input('Replay (Y or N) : ').lower()

while True:

    menu()
    choice = input('Enter yout choice : ').strip()

    if choice == '0':
        print("\nGoodBye 👋")
        break

    elif choice in ('1', '2', '3'):
        level = LEVELS[int(choice) - 1]
        chances = CHANCES[level]
        print(f"\n Great! You have selected the {level} difficulty level.\nLet's start the game! \nYou have {chances} chances to guess the correct number.")
        result = guess(chances)
        if result == 'y':
            continue  # relance le menu
    else:
        print("Invalid choice!")

   