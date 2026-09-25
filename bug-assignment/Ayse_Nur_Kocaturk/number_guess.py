secret = 41
tries = 0
while True:
    guess = input("Guess the number (1-100): ")
    tries = tries + 1
    if guess < secret:
        print("Too low!)
    elif guess >= secret:
        print("Too high!")
    else:
        print(f"Correct! You found it in {tries} tries.")
        break
