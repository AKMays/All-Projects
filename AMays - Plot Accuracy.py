"""
Purpose: Plot accuracy of poll data based on varying sample sizes.
Authors: Adonte Mays
Date: 10/26/2022
Updated: 1/10/2023
"""

import random
import matplotlib.pyplot as plt
import os
import os.path
import string


def poll(percentage, poll_size):
    """
    Purpose: Generate a quasi-random number of people who responded yes to a poll based on an input of percentage and poll size.
    Inputs:
        1. percentage: Percent of pollers that we expect to answer yes. Must be a an integer or float.
        2. poll_size: the number of people in the poll. Must be an integer.
    Return: If preconditions are met, returns the number of voters expected ti answer yes based on a PRNG. If preconditions not met, returns False. 
    """
    if (not isinstance(percentage, int)) and (not isinstance(percentage, float)):
        return False
    if not isinstance(poll_size, int):
        return False
    if (percentage < 0) or (poll_size < 1):
        return False
    yes = 0
    for person in range(poll_size):
        val = random.random()
        if val <= (percentage/100):
            yes = yes + 1
    yes_pct = int((yes/poll_size)*100)
    return yes_pct



def poll_extremes(percentage, poll_size, trials):
    """
    Purpose: To get the maximum and minimum values of yes voters based on a specified number of polling trials against a PRNG.
    Inputs:
        1. percentage: the number of voters expected to say yes. Must be an integer or a float.
        2. poll_size: the number of people in the poll. Must be an integer.
        3. trials: the number of trials we want the PRNG to run through. Must be an integer.
    Return: If preconditions are met, returns minimum and maximum as a list with 2 elements from the specified number of trials run. If preconditions are not met, returns False. 
    """
    if (not isinstance(percentage, int)) and (not isinstance(percentage, float)):
        return False
    if not isinstance(poll_size, int):
        return False
    if not isinstance(trials, int):
        return False
    if (percentage < 0) or (poll_size< 1) or (trials < 1):
        return False
    poll_list = []
    for i in range(trials):
        poll_output = poll(percentage, poll_size)
        poll_list.append(poll_output)
    return min(poll_list), max(poll_list)



def plot_results(percentage, min_poll_size, max_poll_size, step, trials):
    """
    Purpose: To plot the minimum and maximum values from a preset number of polls with increasing poll-sizes. Goal is to illustrate the convergence of results towards the expected result with larger amounts of trials.
    Inputs:
        1. percentage: the percentage of people expected to say yes per poll. Must be an int or float.
        2. min_poll_size: the minimum poll size we want to test. Must be an int.
        3. max_poll_size: the maximum poll size we want to test. Must be an int.
        4. step: the step size between poll sizes. Must be an int greater than 1.
        5. trials: the number of trials per poll size tested. Must be an int.
    Return: returns the error as a ratio between the last outputs of maximum and minimum from the poll_extremes function. Error calculated from the highest poll_size. If invalid input, returns False.
    """    
    if (not isinstance(percentage, int)) and (not isinstance(percentage, float)):
        return False
    if not isinstance(min_poll_size, int):
        return False
    if not isinstance(max_poll_size, int):
        return False
    if not isinstance(step, int):
        return False
    if not isinstance(trials, int):
        return False
    if (percentage < 0) or (min_poll_size < 1) or (max_poll_size < min_poll_size) or (step < 1) or (trials < 1):
        return False
    poll_size = min_poll_size
    poll_size_list = []
    poll_min_vals = []
    poll_max_vals = []
    while poll_size <= max_poll_size:
        poll_extreme_out = poll_extremes(percentage, poll_size, trials)
        poll_min_vals.append(poll_extreme_out[0])
        poll_max_vals.append(poll_extreme_out[1])
        poll_size_list.append(poll_size)
        poll_size = poll_size + step
    plt.plot(poll_size_list, poll_min_vals)
    plt.plot(poll_size_list, poll_max_vals)
    error = (poll_extreme_out[1] - poll_extreme_out[0])/2
    return error



def read_data(file_name):
    """
    Purpose: Read in a csv file with six elements per row and output plots based on the data.
    Inputs:
        1. file_name: the name of a csv file that has six elements per row. The columns being: percentage; min_poll_size; max_poll_size; step; trials; name of the file we will save the plot to.
    Return: None. If input is invalid, will produce an assertion error.
    """
    assert os.path.isfile(file_name)
    assert os.access(file_name, os.R_OK)
    file_obj = open(file_name, 'r')
    for line in file_obj:
        line = line.replace("\n", "")
        text_list = line.split(",")
        plot_results(float(text_list[0]), int(text_list[1]), int(text_list[2]), int(text_list[3]), int(text_list[4]))
        plt.savefig(text_list[5])
        plt.close()
    file_obj.close()



def main():
    read_data("input.csv")

main()
