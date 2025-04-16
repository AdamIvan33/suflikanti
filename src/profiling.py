import math_lib
import sys


number_count = 0
mean = 0
sum = 0
sum_of_squares = 0

for line in sys.stdin:
    numbers_str_list = line.split()
    for number_str in numbers_str_list:
        number_int = int (number_str)
        number_count = math_lib.add(number_count, 1)
        sum = math_lib.add(sum, number_int)
        sum_of_squares = math_lib.add(sum_of_squares, math_lib.n_power(number_int, 2))  #sum_of_squares += number_int**2 

mean = math_lib.div(sum, number_count)

standard_deviation = math_lib.n_root(math_lib.div((math_lib.sub(sum_of_squares, math_lib.mult(math_lib.n_power(mean, 2), number_count))), math_lib.sub(number_count, 1)), 2)


print(standard_deviation)