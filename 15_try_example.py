# try ==> in this block we write the task we want to do
# except ==> in this block we write what to do if exception occurs
# finally ==> this block will execute as soon as the TRY EXCEPT blocks are over


# calculator


def add(a, b):
    return (a + b)


def sub(a, b):
    return (a - b)


def mul(a, b):
    return (a * b)


def div(a, b):
    return (a / b)


def calculate(a, b):
    print(add(a, b))
    print(sub(a, b))
    print(mul(a, b))
    print(div(a, b))

try:
    num1 = (int) (input("enter first number: "))
    num2 = (int) (input("enter 2nd number: "))
    calculate(num1, num2)
except ValueError:
    print("That is an invalid input")
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("Something wrong happened")
finally:
    print("Calculator exited")
