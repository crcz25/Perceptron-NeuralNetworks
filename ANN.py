import fileinput
import json
import math
from pprint import pprint
from itertools import product

def process_input():
    lines = []
    training_data = []
    test_data = []

    for line in fileinput.input():
        lines.append(line.rstrip())
    #pprint(lines)

    d = int(lines[0])
    m = int(lines[1])
    n = int(lines[2])

    print("Dimension of dataset {}".format(d))
    print("Size of training set {}".format(m))
    print("Size of test set {}".format(n))

    training_data = [tuple(map(float, lines[i].split(","))) for i in range(3, 3 + m)]


    if n > 0:
        test_data = [tuple(map(float, lines[i].split(","))) for i in range(3 + m, len(lines))]


    return training_data, test_data



def main():
    training_data, test_data = process_input()

    print('\nTraining data')
    pprint(training_data)

    print('\nTest data')
    pprint(test_data)

if __name__ == '__main__':
    main()