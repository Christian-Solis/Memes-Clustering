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
import collections
# import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

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
    # date_of_meme = list()

    # For loop that extracts the content for each variable
    for line in splitted_input_by_line_break[:-2]:
        # Split input by tabs
        splitted_input_by_tabs = line.split('\t')
        # ID of meme implementation
        id = splitted_input_by_tabs[0]
        # ID of meme
        id_meme = splitted_input_by_tabs[1]
        # Upvotes of the meme
        upvotes = splitted_input_by_tabs[2]
        # Text of meme implementation
        text = splitted_input_by_tabs[3]
        # Date of meme
        # date = splitted_input_by_tabs[4]

        # Append content to corresponding lists
        id_of_meme_implementation.append(id)
        id_of_meme.append(id_meme)
        number_of_upvotes.append(upvotes)
        text_of_implementation.append(text)
        # date_of_meme.append(date)

    print(date_of_meme)

    # #return(stack_of_nodes, number_of_probabilities, probabilities, number_of_queries, queries)

# -----------------------------------------------------------------------------
# Parsing and cleaning process of second dataset
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Word tokenizer that converts text into tokens
# and removes stopwords
# -----------------------------------------------------------------------------

# Tokenize the text
def word_tokenizer(text_of_meme):
   # Tokenizes and stems the text of the meme
   meme_tokens = word_tokenize(text_of_meme)
   # PorterStemmer is an algorithm for removing the commoner morphological
   # and inflexional endings from words in English.
   stemmer = PorterStemmer()
   # Remove the stopwords from the tokens
   # Stop words are words that lack meaning by themselves
   meme_tokens = [stemmer.stem(t) for t in tokens if t not in stopwords.words('english')]
   return meme_tokens

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
