def check_int_input(prompt):
    while True:
        stock = input(prompt)
        if stock.isdigit():
            return int(stock)
        print("Error! Enter a non-negative integer.")

def check_float_input(prompt):
    while True:
        price = input(prompt)
        try:
            if float(price) > 0:
                return round(float(price), 2)
        except ValueError:
            pass
        print("Error! Enter a non-negative number.")

def check_str_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice == "physical" or choice == "digital":
            return choice
        print("Error! Enter Physical or Digital only")