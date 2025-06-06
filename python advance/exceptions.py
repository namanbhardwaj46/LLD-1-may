import os

from DontDivideByZero import DontDivideByZero

def a():

    try:
        raise DontDivideByZero("try not to divide by zero")

    except DontDivideByZero as e:

        print("Custom Exception:", e)
        return "a"


    except ZeroDivisionError as e:
        print("Error:", e)

    except ArithmeticError as e:
        print("Arithmetic Error:", e)
        raise ZeroDivisionError("error as well") from e

    except ValueError as e:
        print("Value Error:", e)


    finally:
        print("Finally block executed")



# a()
# print("hello")


def tryelseblock():
    try:
        print("1. Trying something")
        # Simulating an error
        x = 1 / 1
    except ZeroDivisionError as e:
        print("2. Caught a division by zero error:", e)
    else:
        print("3. No errors occurred, proceeding with the code")
    finally:
        print("4. This will always execute")


tryelseblock()