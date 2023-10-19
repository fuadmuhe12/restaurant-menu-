from guess import Number


def lottery():
    number = Number()
    x = number.roll()
    secret_number = x
    guess_count = 0
    guess_limit = 1

    while guess_count<guess_limit:
        guess = input('guess:')
        try:
            guess = int(guess)	# if the input is non-integer, this fails.
            if guess not in range(0,11):	# if the input is out of desired range, we raise exception ourselves.
             raise Exception("Guess out of range")
        except:
            print("please enter integers only from 0 to 10.")
            continue
        guess_count += 1
        if guess == secret_number:
            print("you won. Thank you for using our service ")
        else:
            print(f'        the number was {x}. Try again and Thank You for using our service.')





