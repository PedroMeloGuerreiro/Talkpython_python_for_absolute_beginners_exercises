print("----------------------------------------")
print("      Even or odd determination v1.0")
print("            Insert 0 to quit")
print("----------------------------------------")

num = 1

while num != 0:
    num_text = input("Please insert a number: ")
    num = int(num_text)

    if num == 0:
        print("You will quit the program")
    elif num % 2 == 0:
        print(f"The number {num} is even!")
        print()
    else:
        print(f"The number {num} is odd!")
        print()
