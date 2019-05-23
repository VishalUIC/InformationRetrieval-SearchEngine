HomeWork 4 : PageRank
----------------------

First Name - Vishal Kumar 
Last Name - Malli Gunasekaran
NetID - vmalli2
UIN - 659597259
                          
Steps to run the  code
------------------------
1. Please run the command �python3 vishal.py <abstract_path> <gold_path>�

Functions that has been used in this project
---------------------------------------------
1. remove_stopwords - This function is used to remove stop words
2. stemming_words - This function is used for stemming
3. removing_pos - This is used for restoring only adjectives and nouns
4. calculate_word_page_rank - This function is used to calculate page rank
5. calculate_bigram - This function is used to calculate bigram from tokens
6. calculate_trigram - This function is used to calculate trigram from tokens
7. gold_ngrams - generate ngrams for the files in gold directory
8. get_top_10 - returns top 10 ngrams based on their page rank or tfidf score
9. get_rank - returns rank of 1st match with the gold file
11. add_node - adds node to the graph
12. add_edge_weight - adds edge between 2 nodes and saves edge weight
13. get_adjacent - returns adjacent nodes for a given node
14. get_edge_weight - return edge weight for given 2 nodes

Output
--------


MRR  1  -  0.055639097744360905
MRR  2  -  0.08007518796992481
MRR  3  -  0.10213032581453625
MRR  4  -  0.12224310776942356
MRR  5  -  0.1362280701754385
MRR  6  -  0.1472556390977441
MRR  7  -  0.1534854994629427
MRR  8  -  0.15752685284640133
MRR  9  -  0.1611191669650313
MRR  10  -  0.1646530015514974

TFIDF MRR  1  -  0.07669172932330827
TFIDF MRR  2  -  0.11278195488721805
TFIDF MRR  3  -  0.1411027568922308
TFIDF MRR  4  -  0.1615914786967421
TFIDF MRR  5  -  0.17587719298245613
TFIDF MRR  6  -  0.1841478696741852
TFIDF MRR  7  -  0.18994808449695635
TFIDF MRR  8  -  0.19539921231650528
TFIDF MRR  9  -  0.19949277956796732
TFIDF MRR  10  -  0.20317699009428306
