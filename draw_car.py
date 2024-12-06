def print_car():
    """
    Prints a simple ASCII art representation of a car.
    """
    long_variable_name = "This is not an example of a very long line"

    car_art = r"""
         ______
        /|_||_\`.__
       (   _    _ _\
       =`-(_)--(_)-'
    """
    print(car_art, long_variable_name)


def car_info():
    """
    Example function that provides car information.
    """
    brand = "Toyota"
    model = "Corolla"
    year = 2022
    print(f"The car is a {year} {brand} {model}.")


if __name__ == "__main__":
    print("Here is your car:")
    print_car()
    car_info()
