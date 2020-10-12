# set of statements doing a specific task
# reusable code


def calculate(a, b):
    print('****CALCULATION STARTS****\n')
    print('a =', a, 'b =', b, "\n")
    print('addition is', (a+b))
    print('subtraction is', (a-b))
    print('multiplication is', (a*b))
    print('division is', (a/b))
    print('\n****CALCULATION ENDS****\n')


calculate(10, 20)
calculate(20, 20)


#reusable code
def profit_calculator(cost, selling_price):
    print("profit is:", (selling_price - cost))
    print("%profit is:", (selling_price - cost) * 100 / cost)


profit_calculator(100, 120)
profit_calculator(50, 100)