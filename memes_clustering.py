# -----------------------------------------------------------------------------
# Name: Christian Ricardo Solís Cortés
# Student ID: A01063685
# Artificial Intelligence
# Assignment: Final Project
# Memes recommendation by clustering techniques
# -----------------------------------------------------------------------------

import heapq
import itertools
import sys
import os

# -----------------------------------------------------------------------------
# Read the dataset file if it changes
# -----------------------------------------------------------------------------

def read_file(filename):
    file_to_read = open(filename)
    print(file_to_read.read())
    file_to_read.close()

# -----------------------------------------------------------------------------
# Parsing and cleaning process
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    # data_set_1 = open('datasets/memes_dataset.in','r')
    # data_set_2 = open('memes_dataset_2.in','r')

    # Specify the file directory to separate datasets from main program
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    # print('File dir ↓', '\n')
    # print(file_dir)

    # Accessing the file in the folder contained in the current folder
    data_set_1 = os.path.join(file_dir, 'datasets/memes_dataset.in')
    read_file(data_set_1)

    # Check if file can be read
    # with open('memes_dataset.in') as f:
    #     first_line = f.readline()
    #     print(first_line)

    # input_reading(data_set_1)

if __name__ == '__main__':
    main()
