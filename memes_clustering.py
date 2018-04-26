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
    # print(file_to_read.read())
    # file_to_read.close()
    input_reading_1(file_to_read)
    # input_reading_2(file_to_read)

# -----------------------------------------------------------------------------
# Parsing and cleaning process of first dataset
# -----------------------------------------------------------------------------

# Clean the dataset to get only the necessary info
def input_reading_1(dataset):
    # Temporal copy of dataset
    temp_dataset = dataset
    # Read the dataset
    dataset_read = dataset.read()
    # Split input by spaces
    splitted_input_by_line_break = dataset_read.split('\n')
    # list of variables
    id_of_meme_implementation = list()
    id_of_meme = list()
    number_of_upvotes = list()
    text_of_implementation = list()
    date_of_meme = list()
    for line in splitted_input_by_line_break:
        # Split input by tabs
        splitted_input_by_tabs = line.split('\t')
        # ID of meme implementation
        id = splitted_input_by_tabs[0]
        # ID of meme
        #id_meme = splitted_input_by_tabs[1]
        # Text of ID implementation
        # upvotes = splitted_input_by_tabs[2]
        # Text of meme implementation
        # text = splitted_input_by_tabs[3]
        # Date of meme
        # date = splitted_input_by_tabs[4:5]

        # Append content to corresponding lists
        id_of_meme_implementation.append(id)
        # id_of_meme.append(id_meme)
        # number_of_upvotes.append(upvotes)
        # text_of_implementation.append(text)
        # date_of_meme.append(date)

    # print(id_of_meme_implementation)
    print(id_of_meme_implementation)
    # Remplace tabulations for *
    # convert_tabs_mult = dataset_read.replace('\t', '*')



    # Remove tabulations from the input
    # input_without_tabs = dataset.read().replace('\t', '')
    # Split input by line breaks
    # splitted_input_by_line_break = input_without_tabs.split('\n')
    # Distint lists of data tipes
    # id_of_meme_implementation = list()
    # id_of_meme = list()
    # print(splitted_input_by_tabs)
    # print(convert_tabs_mult)

    # Separate ID of meme implementation
    #for id in splitted_input_by_line_break:

        # Extract the ID of the meme implementation
        #id_implementation = id[0:8]
        #id_of_meme_implementation.append(id_implementation)

        #id_1 = id.split()
        #print(id_1  )
        # id_temp = id.split(' ', 1)
        # print(id_temp)
        # Extract the ID of the meme

        # id_meme = id[9:]

    # print (id_of_meme_implementation)

    # # Save nodes and number of probabilities in stack
    # stack_of_nodes = splitted_input_by_line_break[0]
    # number_of_probabilities = int(splitted_input_by_line_break[1])
    # # Save probabilities in a list
    # probabilities = list()
    # for line in range(2, 2 + number_of_probabilities):
    #     probabilities.append(splitted_input_by_line_break[line])
    # # Save number of queries in stack
    # number_of_queries = int(splitted_input_by_line_break[2 + number_of_probabilities])
    # # Save queries in a list
    # queries = list()
    # for line in range(3 + number_of_probabilities, 3 + number_of_probabilities + number_of_queries):
    #     queries.append(splitted_input_by_line_break[line])
    #
    # # print(stack_of_nodes)
    # # print(number_of_probabilities)
    # # print(probabilities)
    # # print(number_of_queries)
    # # print(queries)
    #
    # # Send respective values to functions
    # split_nodes(stack_of_nodes)
    # split_probabilites(probabilities)
    # split_queries(queries)
    #
    # #return(stack_of_nodes, number_of_probabilities, probabilities, number_of_queries, queries)

# -----------------------------------------------------------------------------
# Parsing and cleaning process of second dataset
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    # Specify the file directory to separate datasets from main program
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    # print('File dir ↓', '\n')
    # print(file_dir)

    # Accessing the file in the folder contained in the current folder
    data_set_1 = os.path.join(file_dir, 'datasets/memes_dataset.in')
    # data_set_2 = os.path.join(file_dir, 'datasets/memes_dataset_2.in')
    read_file(data_set_1)
    # read_file(data_set_2)

if __name__ == '__main__':
    main()
