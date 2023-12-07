def is_prime(num):  # function to check if a given number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start, end):  # function to display prime
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")


# main program
def main():
    print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
    print("Created by: Per Virgil B. Wabe")
    print("\nProblem: Create a Python program that displays all prime numbers within a range:")
    print("\n RULES TO CONSIDER:")
    print("[1] If number [start] is a negative number. The program will prompt a message: 'Enter a non-negative "
          "number' ")
    print("[2] If number [end] is less than number [start]. The program will prompt a message 'Enter a number "
          "greater than number [start]'")
    print("[3] If the user enter the number “0”, the program will terminate. ")
    print("\nEnter a number [start]: -1 ")
    print("Enter a non-negative number:")

    while True:
        start = int(input("\nEnter a number [start]: "))

        if start < 0:
            print("Enter a non-negative number.")
        elif start == 0:
            print("Program terminated.")
            break
        else:
            while True:
                end = int(input(f"Enter a number greater than {start}: "))
                if end > start:
                    display_primes(start, end)
                    break
                else:
                    print(f"Enter a number greater than {start}.")


if __name__ == "__main__":
    main()
