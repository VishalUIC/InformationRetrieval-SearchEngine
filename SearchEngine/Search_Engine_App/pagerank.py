import graph as Graph_Class
import json


global_access_page_Rank = {}

def calculate_word_page_rank(page_rank_score, Graph_obj, abstract_words):
    count = 0
    alpha = 0.85
    pi = 1/len(abstract_words)

    for x in abstract_words:
        sum = 0
        for y in Graph_obj.get_adjacent(x):
            wyz_sum = 0
            for z in Graph_obj.get_adjacent(y):
                wyz_sum += Graph_obj.get_edge_weight(y, z)
            if wyz_sum != 0:
                sum += (Graph_obj.get_edge_weight(y, x)/wyz_sum) * page_rank_score[y]
            page_rank_score[x] = alpha * sum + (1 - alpha) * pi


def main():

    global global_access_page_Rank
    with open('webpagesdump.json') as f:
        webpages = json.load(f)

    page_rank_score = {}
    node_length = len(webpages)
    urls = list(webpages.keys())

    graph_obj = Graph_Class.Graph()
    for x in urls: # main urls
        graph_obj.add_node(x)
        page_rank_score[x] = 1/node_length
    for x in urls:  # main urls
        for y in webpages[x]['links']: # outlinks here
            graph_obj.add_edge_weight(x, y)

    iter = 0
    while(iter < 10):
        iter += 1
        _ = calculate_word_page_rank(page_rank_score, graph_obj, urls)

    global_access_page_Rank = page_rank_score


#main()