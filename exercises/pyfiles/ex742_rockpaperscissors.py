def filter_options(option):
    for digit in [str(i) for i in range(10)]:
        option = option.replace(digit, "")

        if option.isalpha():
            break

    option = option.lower()

    if option in ["rock", "paper", "scissors"]:
        return option
    else:
        return None