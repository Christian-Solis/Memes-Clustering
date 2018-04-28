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
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint

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

    # Number of clusters
    number_of_clusters = 4

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
    # word_tokenizer(text_of_implementation)
    cluster_memes(text_of_implementation, number_of_clusters)

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
    # Tokenizes and stems the text of the meme
    meme_tokens = word_tokenize(text_of_meme)
    # PorterStemmer is an algorithm for removing the commoner morphological
    # and inflexional endings from words in English.
    stemmer = PorterStemmer()
    # Remove the stopwords from the tokens
    # Stop words are words that lack meaning by themselves
    meme_tokens = [stemmer.stem(t) for t in meme_tokens if t not in stopwords.words('english')]
    return meme_tokens

# -----------------------------------------------------------------------------
# Function that clusters the tokenized memes
# Receives the tokenized memes and number of clusters given
# The tf-idf value increases proportionally to the number of
# times a word appears in the document
# KMeans usage, assumes that we know the number of clusters,
# then it clusters randomly the n clusters (centroids),
# and the distance between each node and the centroid with euclidian distance
# (Pitagoras Theorem = dist((x, y), (a, b)) = √(x - a)² + (y - b)²).
# Then each node its grouped with its nearest centroid.
# Finally, new centroids are calculated and the process repeates again.

# -----------------------------------------------------------------------------

# Cluster the memes
def cluster_memes(text_of_implementation, number_of_clusters):
    # TfidfVectorizer converts a collection of documents
    # into a matrix of TF-IDF features
    # Term Frequency–inverse Document Frequency
    # word_tokenizer call, use of stopwords, max document frecuency,
    # and converstion to lowercase
    vectorizer = TfidfVectorizer(tokenizer=word_tokenizer,
                                stop_words=stopwords.words('english'),
                                max_df=0.9,
                                min_df=0.1,
                                lowercase=True)
    # Builds a tf-idf matrix for the memes
    # Transforms meme tokens into matrix
    tfidf_matrix = vectorizer.fit_transform(text_of_implementation)

    # Usage of KMeans clustering algorithm
    # K Means tries to group clusters with similar characteristics
    # by maximizing inter-cluster variation and minimizing intra-cluster
    k_means = KMeans(n_clusters=number_of_clusters)
    # Compute KMeans clustering
    k_means.fit(tfidf_matrix)
    # Dictionary of clusters
    meme_clusters = collections.defaultdict(list)

    for i, label in enumerate(k_means.labels_):
        # Append the matrix to meme clusters
        meme_clusters[label].append(i)
    # Get the dictionary of meme clusters

    # Loop to print number of cluster and nodes of the clusters
    # Iterate n times the number of clusters
    for cluster in range(number_of_clusters):
        print ("Cluster ",cluster,":")
        # Enumerate the nodes in the cluster
        for i,meme in enumerate(meme_clusters[cluster]):
            print ("\Meme ",i,": ",text_of_implementation[meme])


    # return dict(meme_clusters)

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
