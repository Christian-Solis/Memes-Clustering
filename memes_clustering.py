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
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# -----------------------------------------------------------------------------
# Open the first dataset file
# -----------------------------------------------------------------------------

def read_file_1(filename):
    file_to_read = open(filename)
    input_reading_1(file_to_read)

# -----------------------------------------------------------------------------
# Open the second dataset
# -----------------------------------------------------------------------------

def read_file_2(filename):
    file_to_read = open(filename)
    input_reading_2(file_to_read)

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
    for line in splitted_input_by_line_break[:-1]:
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

    dataset.close()
    # return(id_of_meme_implementation, id_of_meme, number_of_upvotes)
    word_tokenizer(text_of_implementation)

# -----------------------------------------------------------------------------
# Parsing and cleaning process of first dataset
# -----------------------------------------------------------------------------

# Clean the dataset to get only the necessary info
def input_reading_2(dataset):
    # Temporal copy of dataset
    temp_dataset = dataset
    # Read the dataset
    dataset_read = dataset.read()
    # Split input by spaces
    splitted_input_by_line_break = dataset_read.split('\n')
    # list of variables
    id_of_meme = list()
    url_slug_of_meme = list()
    meme_name = list()
    url_of_meme = list()

    # For loop that extracts the content for each variable
    for line in splitted_input_by_line_break[:-1]:
        # Split input by tabs
        splitted_input_by_tabs = line.split('\t')
        # ID of meme
        id_meme = splitted_input_by_tabs[0]
        # URL slug of meme
        slug = splitted_input_by_tabs[1]
        # Meme name
        name = splitted_input_by_tabs[2]
        # URL of meme
        url = splitted_input_by_tabs[3]

        # Append content to corresponding lists
        id_of_meme.append(id_meme)
        url_slug_of_meme.append(slug)
        meme_name.append(name)
        url_of_meme.append(url)

    dataset.close()
    # return(id_of_meme, url_slug_of_meme, meme_name, url_of_meme)

# -----------------------------------------------------------------------------
# Word tokenizer that converts text into tokens
# and removes stopwords
# -----------------------------------------------------------------------------

# Tokenize the text
def word_tokenizer(text_of_meme):

    for each_meme in text_of_meme:
        # Tokenizes and stems the text of the meme
        meme_tokens = word_tokenize(each_meme)
        # PorterStemmer is an algorithm for removing the commoner morphological
        # and inflexional endings from words in English.
        stemmer = PorterStemmer()
        # Remove the stopwords from the tokens
        # Stop words are words that lack meaning by themselves
        meme_tokens = [stemmer.stem(t) for t in meme_tokens if t not in stopwords.words('english')]
        # print(meme_tokens)

# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    # Specify the file directory to separate datasets from main program
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    # Accessing the file in the folder contained in the current folder
    data_set_1 = os.path.join(file_dir, 'datasets/memes_dataset.in')
    data_set_2 = os.path.join(file_dir, 'datasets/memes_dataset_2.in')
    read_file_1(data_set_1)
    read_file_2(data_set_2)

if __name__ == '__main__':
    main()
