# Write a Python function called max_num()to find the Max of three numbers.

def max_num(num1, num2, num3):
    return max([num1, num2, num3])


print(max_num(1, 5, 10))
print(max_num(50, 40, 30))
print(max_num(8, 4, 7))


# Write a Python function called mult_list()  to multiply all the numbers in a list.
def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod


print(mult_list([1, 2, 3]))
print(mult_list([4, 5, 6]))
print(mult_list([0]))

# Write a Python function called rev_string() to reverse a string.


def rev_string(string):
    return string[::-1]


print(rev_string('Hello World'))
print(rev_string('My name is'))
print(rev_string('Slim Shady'))

# Write a Python function called num_within() to check whether a number falls in a given range.


def num_within(x, a, b):
    return x in range(a, b+1)


print(num_within(1, 1, 2))
print(num_within(1, 2, 3))
print(num_within(3, 2, 4))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1], [1, 1]]


def pascal(n):
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)


pascal(10)
