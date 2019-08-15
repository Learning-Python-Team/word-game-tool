#please edit this below import, this may be wrong
from .word_to_score import point_conversion

#this does not consider the premium squares 
#the following function finds and returns the highest scoring word from a list of words
def compare_words(list_of_words):
    scores=[]
    for word in list_of_words:
        scores.append(point_conversion(word))
    index_best_word=scores.index(max(scores))
    return list_of_words[index_best_word]

list_of_words=['mom','dad','Queue']
print(compare_words(list_of_words))
