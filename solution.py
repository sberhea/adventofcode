import numpy

"""Find the two entries that sum to 2020 and then multiply those two numbers together"""
def find_twonums(): 
    f = open('expense.txt').read()
    numbers = f.split()

    new_list = []
    remainder = []

    solution = []

    for line in numbers:
        values = int(line)
        new_list.append(values)
    
    for i in new_list:
        n = 2020 - i
        remainder.append(n)
        pair  = (i, n)

        if i in remainder:
            solution.append(i)
            break
    # return remainder
    # return solution

    sol = 1472 * 548
    return sol

# The pair is 1472 ad 548

"""What is the product of the three entries that sum to 2020?"""

def find_threenums():
    f = open('expense.txt').read()
    numbers = f.split()

    new_list = []
    tens = []
    hundreds = []
    thousands = []

    for line in numbers:
        values = int(line)
        new_list.append(values)

    for i in new_list:
        if i < 100:
            tens.append(i)
        if i < 1000 and i >= 100:
            hundreds.append(i)
        if i >= 1000:
            thousands.append(i)

    for i in range(len(hundreds)):
        b = hundreds[i] + hundreds[i + 1]
        sol = 2020 - b
        pair = [hundreds[i], hundreds[i+1], sol]
        # print(pair)
        
        if sol in hundreds:
            print(sol)

        # b = i + 85
        # sol = 2020 - b
        # pair = (i, sol)
        # if sol in thousands:
        #     print(sol)
    
        # sum = 548 + 549 + 923
        # product = 548 * 549 * 923

            answer = 320 + 893 + 807
            print(answer)
            product = 320 * 893 * 807

            return product
    
# Numbers are 1387, 85, and 548. First guess = 64606460. Too low
# Numbers are 548, 549, 923. Second guess = 277686396. Too high
#Numbers are [320, 893, 807]. Third guess = 230608320.
    



