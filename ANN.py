import fileinput
import json
import math
from pprint import pprint
from random import random
from itertools import product

learning_rate = 0.01

def calculate_output(weights, inputs):
    s = 0
    for i in range(len(weights)):
        s += weights[i] * inputs[i]

    if s > 0:
        return 1
    return 0

# Return None if it's not linearly 
def train_ann(training_data):
    number_inputs = len(training_data[0]) - 1
    
    error_last_iteration = 100000000

    weights = [random() for x in range(number_inputs)]
    
    iteration_number = 0
    
    while(error_last_iteration > 0):
        error_iteration = 0
        for row in training_data:
            y_cap = calculate_output(weights, row[:-1])
            delta = row[-1] - y_cap
            
            for i in range(len(weights)):
                weights[i] += delta * learning_rate * row[i]
            
            error_iteration += delta ** 2
            

        iteration_number += 1
        if iteration_number > 5000:
            return None
            
        error_last_iteration = error_iteration
    
    return weights

def process_input():
    lines = []
    training_data = []
    test_data = []

    for line in fileinput.input():
        lines.append(line.rstrip())

    d = int(lines[0])
    m = int(lines[1])
    n = int(lines[2])

    #print("Dimension of dataset {}".format(d))
    #print("Size of training set {}".format(m))
    #print("Size of test set {}".format(n))

    training_data = [tuple([1]) + tuple(map(float, lines[i].split(","))) for i in range(3, 3 + m)]

    if n > 0:
        test_data = [tuple(map(float, lines[i].split(","))) for i in range(3 + m, len(lines))]

    return training_data, test_data



def main():
    training_data, test_data = process_input()

    """
    print('\nTraining data')
    pprint(training_data)

    print('\nTest data')
    pprint(test_data)"""
    
    neuron = train_ann(training_data)
    
    if neuron:
        for test in test_data:
            
            print(calculate_output(neuron, tuple([1]) + test))
            
    else:
        print('no solution found')

if __name__ == '__main__':
    main()