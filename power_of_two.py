#!/usr/bin/env python3
# Created By: Joyceline
# Created on: November 16, 2026
# This program asks the user for a positive whole number
# and calculates the squares from 0 up to that number using a for loop.


def main():
    # initializing variables
    number = 0
    square = 0

    # Get the user's number
    try:
        number_str = input("Enter a positive whole number: ")
        number_int = int(number_str)

        if number_int < 0:
            print(
                "{} is an invalid entry. Please enter a positive whole number.".format(
                    number_str
                )
            )
        else:
            # Calculate the square number using a for loop
            for i in range(number_int + 1):
                square = i**2
                print(str(i) + "^2 = " + str(square))

    except ValueError:
        print("{} is an invalid input. Please enter a whole number.".format(number_str))

    finally:
        print("Thanks for playing!!")


if __name__ == "__main__":
    main()
