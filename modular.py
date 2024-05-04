"""
Name: David Crowley
Date: May the 4th be with you, 2024
Description: Exemplar for the Functions practical

The idea for this project is a city atlas where you can get information
about a variety of cities you select.

Scope: Only the name variable was declared global since it is
referenced by welcome, get_city and bye functions. All other
variables are declared locally with information flowing as arguments
or return values
"""

"""
How this exemplar meets the requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exemplar meets only basic requirements :
- 3 implemented functions + main
- no test cases for invalid input
- no control structures or logical operators
- no flowcharts for planned logic

To meet the requirement of 3 implemented methods besides main, this exemplar 
implements two call chains :
- main -> welcome
- main -> get_city_info -> get_population

The methods get_area and bye are not implemented (and are not fully described
in the functions diagram either)

To meet the 'at least one function with a return value and one function 
with a parameter' requirement, the get_population function has both. Both other
functions are procedures (no parameters or return values).

For communication requirements, test cases and scope explanations are provided 
within the docstrings and the file header comment, respectively.
"""

# global variable for the user's name
name = ""


def welcome():
    """
    Test cases for the personalized message :
    one name : "David"
        -> prints "Great David! Let's begin..."
    multiple names : "John Jehosephat Jeremiah"
        -> prints "Great John Jehosephat Jeremiah! Let's begin..."
    random characters : "abda-31345n"
        -> prints "Great abda-31345n! Let's begin..."
    """
    global name
    print("Welcome to my city almanac!\n")
    name = input("What is your name? > ")
    print(f"Great {name}! Let's begin...\n")


def get_population(city: str) -> int:
    """
    Test cases :
    city in database : "Toronto" -> 6_431_000

    (invalid input cases are not required, but could include
    a misspelled city name or a city not in the database)

    We can't run these tests without setting up the database first.

    This implementation gives mock values for the population instead.
    """
    print(f"...looking up {city}'s population")  # mock lookup of city's population

    import random  # to mock a random population value

    return random.randint(75_000, 30_000_000)  # return mocked population


def get_city_info():
    """
    These test cases depend on the called functions working properly. Those
    should be tested first.

    Test cases for displaying the results with _ as the thousands separator:
    city in database : "Toronto"
        -> print "Toronto's population is 6_431_000."
    lowercase letters : "toronto"
        -> print "Toronto's population is 6_431_000."
    uppercase letters : "TORONTO"
        -> print "Toronto's population is 6_431_000."

    (cases for invalid cities are not required but could include printing a
    special message depending on the type of error returned by get_population.)
    """
    city = input(f"{name}, what city interests you? > ")
    city = city.capitalize()  # correct case before using city in lookup functions
    population = get_population(city)
    print(f"{city}'s population is {population:_}.")


def main():
    welcome()
    get_city_info()


main()
