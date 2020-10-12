# function name, function parameters, function body  ---  def keyword
# anonymous function  ---  lambda keyword


# def square(number):
#     return number ** 2


sqr_lambda = lambda number: number ** 2

print(type(sqr_lambda))
print(sqr_lambda(5))


list1 = [12, 45, 98, 78, 54, 13]


# def odd_Numbers(l):
#     new_list = []
#     for number in list1:
#         if number % 2 == 1:
#             new_list.append(number)
#     return new_list

new_list = list(filter(lambda num: (num%2 == 1), list1))
print(new_list)


adder = lambda x, y: x + y
print(adder(45, 56))
