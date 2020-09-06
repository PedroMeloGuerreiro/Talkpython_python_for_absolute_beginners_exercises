def main():
    max_mm_number = 100
    attempt_limit = 5

    print_info()
    guess_mm(max_mm_number, attempt_limit)


def print_info():
    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")

    print("Guess the number of M&Ms and you get lunch on the house!")
    print()


def guess_mm(mm_number, attempt_max):
    import random
    mm_count = random.randint(1, mm_number)
    attempts = 0
    success = False

    while attempts < attempt_max:
        guess_text = input("How many M&Ms are in the jar? ")
        guess = int(guess_text)
        attempts += 1

        if mm_count == guess:
            print(f"You got a free lunch in {attempts} attempts! It was {guess}.")
            success = True
            break
        elif guess < mm_count:
            print("Sorry, that's too LOW!")
        else:
            print("That's too HIGH!")

    if not success:
        print(f"You used your {attempt_max} attempts and failed. There were {mm_count} M&M's in the jar. No free "
              f"lunch for you!")


if __name__ == '__main__':
    main()
