def menu():
    print("="*50)
    print("Welcome to the Number Guessing Game!")
    print("="*50)
    print('\n')
    print("Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)")
    print('\n')

def guess(nb_chances:int):
    
    import random

    nombre = random.randint(1,10)

    attempts = 0

    while 1:
        guess = int(input('Enter your guess : '))
        print('\n')

        if nombre == guess and nb_chances > 0:
            attempts += 1
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess == 0:
            break

        elif nombre != guess and nombre < guess and nb_chances > 0:
            print(f'Incorrect! Please retry, The number is less than {guess}')
            print('\n')
            nb_chances -= 1
            attempts += 1

        elif nombre != guess and nombre > guess and nb_chances > 0:
            print(f'Incorrect! Please retry, The number is greater than {guess}')
            print('\n')
            nb_chances -= 1
            attempts += 1
        
        elif nb_chances == 0:
            print("You're out of chances 😅 See you next time !")
            break
while 1:

    menu()
    choice = input('Enter yout choice : ')
    print("="*25)

    if choice == '1':
        print("Great! You have selected the Easy difficulty level.\nLet's start the game!")
        print('\n')
        print('You have 10 chances to guess the correct number.')
        print('\n')
        guess(10)
        replay = input('Replay (Y or N) : ')
        if replay == "y":
            guess(10)
        elif replay == "n":
            pass
        else:
            "Unknown choice !"

    elif choice == '2':
        print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
        print('You have 5 chances to guess the correct number.')

    elif choice == '3':
        print("Great! You have selected the Hard difficulty level.\nLet's start the game!")
        print('You have 3 chances to guess the correct number.')

    elif choice == '0':
        break

    else:
        print('Invalid choice!')
                
                


