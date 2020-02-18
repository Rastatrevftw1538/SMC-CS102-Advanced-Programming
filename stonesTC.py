# Trevor Cardoza
# CS 102 Spring 2020
# Febuary 13th
# Program: weights.
# Asks for two weights from two different individuals,
# converts them to stones and kg, then averages them


def main():  # Main function
    print("Welcome to the weight converter!\n")
    # Name
    Person1 = str(input("Name of person 1: "))
    # Weight in pounds
    Weight1 = float(input(Person1 + "'s weight in pounds: "))
    # Pounds to stones
    stone_convert1 = int(Weight1 * 0.071429)
    # Remainder of the weight by the amount of stones in one pound
    remainder1 = int(Weight1 % 14)
    # Pounds to Kilograms
    kg1 = float(Weight1 * 0.4535924)
    print(
        Person1+"'s",
        "weight is",
        stone_convert1,
        "Stones",
        remainder1,
        "and",
        round(kg1, 2),
        "kg.",
    )
    # Name
    Person2 = str(input("\nName of person 2: "))
    # Weight in pounds
    Weight2 = float(input(Person2 + "'s weight in pounds: "))
    # Pounds to stones
    stone_convert2 = int(Weight2 * 0.071429)
    # Remainder of the weight by the amount of stones in one pound
    remainder2 = int(Weight2 % 14)
    # Pounds to Kilograms
    kg2 = float(Weight2 * 0.4535924)
    print(
        Person2+"'s",
        "weight is",
        stone_convert2,
        "Stones",
        remainder2,
        "and",
        round(kg2, 2),
        "kg.",
    )
    # Average weight between the two
    AverageWeight = float((Weight2 + Weight1) / 2)
    # Average stone between the two
    Average_stone_convert = int((stone_convert1 + stone_convert2) / 2)
    # Remainder for the average stone
    Average_remainder = int(AverageWeight % 14)
    # Average kilograms between the two
    Average_kg = float((kg1 + kg2) / 2)
    print("\nAverage weight in pounds is", AverageWeight)
    print(
        "Average weight in stones is",
        Average_stone_convert,
        "stone",
        Average_remainder,
    )
    print("Average weight in kilograms is", round(Average_kg, 2), "\n")
    print("Thank you for using stonesTC!")


main()  # Start main function on run
