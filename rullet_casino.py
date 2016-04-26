#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def zero_return(attempts, value_to_check):
    result = []
    for attempt in range(0, attempts, 1):
        random_value = random.randint(0, 40)
        if random_value == value_to_check:
            result.append(0)
        else:
            result.append(1)
    return result


if __name__ == "__main__":
    repeat_confirm = input("Do you want to start press Y. If don't press any key: ")
    while repeat_confirm == 'Y' or repeat_confirm == 'y':
        lucky_value = int(input("Input Lucky Value: "))
        lucky_attempts = int(input("Input attempts Amount: "))
        result_array = zero_return(lucky_attempts, lucky_value)

        attempts_counter = 0
        for i in result_array:
            attempts_counter += 1
            if i == 0:
                print("Congratulations your attempt: " + str(attempts_counter) + " is successful with: " + str(
                    lucky_value) + " value")
            else:
                print("Your attempt: " + str(attempts_counter) + " is unsuccessful")
        repeat_confirm = input("\n" + "Do you want to try more? If Yes print Y. If no press any key!")
