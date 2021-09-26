
from function_class import Calculator
from converter_class import Converter


def main():
    """
        main-program
        purpose: handles user input and prints
                 information to the console.
    """
    print("\t\t\t\t\t\t\t\tScientific Calculator\n\n\t\t\tFor Example: sin(rad(90)) + 50% * (sqrt(16)) + round(1.42^2)" +
          "- 12mod3")

    choice = input("Press '1' to calculate figures\nPress '2' for weight converter\nEnter quit to exit... "
                   "\n>> ")
    while True:

        if choice == "1":
            while True:
                k = input("\nWhat is ")
                calc = Calculator(k)
                if k == 'quit':
                    main()   # Revert back to the beginning
                Calculator.result(calc)
        elif choice == "2":
            while True:
                first = input("\n\nTo convert weight from pounds to kilogram press '1'\n To convert weight from kilogram to "
                              "pounds press '2'\n Press 'quit' to go back to menu...")

                if first == "1":
                    weight1 = input("\nwhat is your weight in pounds: ")
                    converter = Converter(weight1)
                    print(f"Your weight in pounds is: {round(converter.convert_pounds_to_kilogram())}lbs")

                elif first == "2":
                    weight2 = input('\nwhat is your weight in kilogram: ')
                    converter = Converter(weight2)
                    print(f"Your weight in pounds is: {round(converter.convert_kilogram_to_pounds())}kg")

                elif first == "quit":
                    main()

        if choice == "quit":
            break


if __name__ == '__main__':
    main()
