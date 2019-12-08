#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program finds the largest value


import random


def sum_of_numbers(list_of_numbers):
    # this function determines what the biggest number in the list is.

    largest = list_of_numbers[0]
    for single_num_list in range(0, len(list_of_numbers)):
        if list_of_numbers[single_num_list] > largest:
            largest = list_of_numbers[single_num_list]

    return largest


def main():
    # this function uses a list

    random_numbers = []
    biggest = 0

    # input
    print("The Numbers in the List are: ")
    for loop_counter in range(0, 9):
        single_number = random.randint(0, 1000)
        random_numbers.append(single_number)
        print("[{0}] ".format(single_number), end="")
    print("")

    biggest = sum_of_numbers(random_numbers)

    print("The Largest Number is: {0} ".format(biggest))


if __name__ == "__main__":
    main()
