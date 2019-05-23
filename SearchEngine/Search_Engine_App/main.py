import tfidf as tf
import pagerank as pg
from collections import defaultdict
import math
from tkinter import *


def idf(df, N):
    return math.log(N/df,2)


def similarity(lengths_of_document_dict, query_tf, query_number, document_number, index_file):
    collection = len(lengths_of_document_dict)
    num = 0
    for token, frequency in query_tf.items():
        if token in index_file:
            if document_number in index_file[token]:
                num += frequency * idf(len(index_file[token]), collection) * index_file[token][document_number] * idf(
                    len(index_file[token]), collection)

    denom = lengths_of_document_dict[document_number] * tf.vector_length_of_query(query_tf, index_file)

    if denom == 0:
        return 0

    return num / denom


def execute_query(lengths_of_document_dict, index_file, query_list):
    retrieved_dict = {}
    collection_urls = list(lengths_of_document_dict.keys())

    try:

        query_tf = defaultdict(int)
        for word in query_list.split():
            word = tf.format_token_with_stemming(word)
            if len(word) > 2:
                query_tf[word] += 1
        for j in collection_urls:
            retrieved_dict[j] = similarity(lengths_of_document_dict, query_tf, "", j, index_file)

        return retrieved_dict

    except Exception as e:
        print("Error processing URL " + e)


def hmean(a,b):
    return 2*a*b/(a+b)


def tfidfSearch(query):
    return execute_query(tf.global_access_documents_length, tf.global_access_inverted_index, query)
    #return sorted(res.items(), key=lambda x: x[1], reverse=True)


global_result = []


def pageRankSearch(query):
    global global_result
    tf_res = execute_query(tf.global_access_documents_length, tf.global_access_inverted_index, query)
    #tf_res = {key:value for key, value in tf_res}
    print("TF-IDF Result")
    print(sorted(tf_res.items(), key=lambda x: x[1], reverse=True)[:10])
    tf_res1 = sorted(tf_res, key=tf_res.get, reverse=True)[:35]

    result = {key:hmean(tf_res[key],pg.global_access_page_Rank[key]) for key in tf_res1}
    listbox.delete(0, END)
    top_ten_urls = sorted(result.items(), key=lambda x: x[1], reverse=True)
    print("Page Rank Result")
    print(top_ten_urls[:10])

    for i in top_ten_urls[:10]:
        listbox.insert(END, i[0])

    global_result = top_ten_urls



def main():
    print("TF-IDF is running...")
    tf.main()
    print("Page rank algorithm is running...")
    pg.main()
    print("Application Started")
    # res = tfidfSearch("uic computer")
    # res_sorted = sorted(res.items(), key=lambda x: x[1], reverse=True)
    # print(res_sorted[:20])
    # res = pageRankSearch("uic computer")
    # res_sorted = sorted(res.items(), key=lambda x: x[1], reverse=True)
    #
    # print(res_sorted[:20])


def show_more_results():
    listbox.delete(0, END)
    for i in global_result[:30]:
        listbox.insert(END, i[0])


main()

window = Tk()
window.configure(background="white")
window.title("UIC Search Engine")
window.geometry('3000x3000')
txt = Entry(window, width=30)
txt.grid(column=4, row=4)
btn1 = Button(window, text="Search", command=lambda: pageRankSearch(txt.get()))
btn1.grid(column=3, row=5)
btn2 = Button(window, text="More results", command=lambda: show_more_results())
btn2.grid(column=3, row=6)
listbox = Listbox(window, width=80, height=35)
listbox.grid(column=4, row=20)

window.mainloop()

