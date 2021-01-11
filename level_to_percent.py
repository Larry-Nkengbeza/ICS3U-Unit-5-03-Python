# This program was created by Larry Nkengbeza
# This program was created in January 2020
# This program converts level to percentage


def level_to_percentage(level):
    # comment here
    percentage = 0

    if level == "R" or level == "r":
        percentage = 30
    elif level == "-1":
        percentage = 51
    elif level == 1:
        percentage = 55
    elif level == "+1":
        percentage = 59
    elif level == "-2":
        percentage = 61
    elif level == 2:
        percentage = 65
    elif level == "+2":
        percentage = 69
    elif level == "-3":
        percentage = 71
    elif level == 3:
        percentage = 75
    elif level == "+3":
        percentage = 79
    elif level == "-4":
        percentage = 81
    elif level == 4:
        percentage = 89
    elif level == "+4":
        percentage = 99

    return percentage


def main():
    # Input
    user_input = int(input("Enter a level: "))
    print("")
    (percentage_passed_back) = level_to_percentage(user_input)

    print("The percentage is: " + str(percentage_passed_back))


if __name__ == "__main__":
    main()
