import os
import regex as re
import string,nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords as stpWords
from collections import defaultdict
import math
import operator
import json

collection = 0
stopwords = stpWords.words('english')


def format_token(token):
    xml_pattern = re.compile("<.[^(><.)]+>")
    if xml_pattern.match(token):
        return ""
    formatted_token = re.sub('[^A-Za-z]', '', token).lower()
    return formatted_token


def format_token_with_stemming(token):
    stemmer = PorterStemmer()
    formatted_token = format_token(token)
    if formatted_token not in stopwords and token not in stopwords:
        return stemmer.stem(formatted_token)
    else:
        return ""


def create_tokens_with_stemming():
    formatted_tokens = []
    try:
        for file in os.listdir("citeseer"):
            fp = open("citeseer/"+file)
            data = fp.read()
            tokens = data.split()
            for token in tokens:
                processed_token = format_token_with_stemming(token)
                if len(processed_token) >= 1:
                    formatted_tokens.append(processed_token)
    except:
        print("Error processing file " + file)
    return formatted_tokens


def vector_length_of_query(query_tf, index_file):
    length = 0
    for word in query_tf:
        if word in index_file:
            length += (idf(len(index_file[word]), collection) * query_tf[word])**2
    
    return math.sqrt(length)


def idf(df, N):
    return math.log(N/df,2)
    
    
def length_of_documents(index_file):
    length_of_documents_dict = defaultdict(int)
    for token in index_file:
        for docs in index_file[token]:
            length_of_documents_dict[docs] += (idf(len(index_file[token]), collection) * index_file[token][docs])**2

    for doc in length_of_documents_dict:
        length_of_documents_dict[doc] = math.sqrt(length_of_documents_dict[doc])
    
    return length_of_documents_dict


def create_inverted_index():
    global collection
    index_file = {}
    doc_no = 1
    try:
        with open('webpagesdump.json') as f:
            webpages = json.load(f)
        docs = list(webpages.keys())
        collection = len(docs)
        for file in docs:

            tokens = webpages[file]['content'].split()
            for token in tokens:
                processed_token = format_token_with_stemming(token)
                if len(processed_token) > 2:

                    if processed_token not in index_file:
                        index_file[processed_token] = {file: 1}
                    elif file not in index_file[processed_token]:
                        index_file[processed_token][file] = 1
                    else:
                        index_file[processed_token][file] += 1
            doc_no += 1
    except Exception as e:
        print("Error processing file " + file)
    return index_file


global_access_inverted_index = {}
global_access_documents_length = {}


def main():
    global global_access_inverted_index
    global global_access_documents_length

    inverted_index = create_inverted_index()
    lengths_of_document_dict = length_of_documents(inverted_index)
    global_access_inverted_index = inverted_index
    global_access_documents_length = lengths_of_document_dict


#main()
