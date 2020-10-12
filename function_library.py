def add(list_of_num):
    sum = 0
    for number in list_of_num:
        sum = sum + number
    return sum


def print_even(list_of_num):
    for num in list_of_num:
        if num % 2 == 0:
            print(num, end=" ")
    print()