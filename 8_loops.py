# For loop
# While loop

# in range function

# if we give only 1 value, it will start from 0 till the value, jumping 1 number at a time
for counter in range (5):
    print('for counter', counter)


# if we gice 2 values, it will start from the first value, till the 2nd value, jumping 1 number at a time
for counter in range (4, 10):
    print ('hello', counter)

# if we give 3 values, it will start from the 1st, go till the 2nd, and jumping factor is 3rd
for counter in range (1, 11, 3):
    print ('hi', counter)


# buying chocolate
# if condition satisfies, it will enter the loop body
# after executing the loop body, it will again check the condition
chocolates_to_buy = 5
chocolates_in_hand = 0

while chocolates_in_hand < chocolates_to_buy:
    print("Buying another chocolate")
    chocolates_in_hand = chocolates_in_hand + 1
    print("Now chocolates in hand is", chocolates_in_hand)


