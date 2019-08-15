#this does not consider the premium squares 
#the following function finds and returns the highest scoring word from a list of words
def compare_words(list_of_words):
    scores=[]
    for word in list_of_words:
        scores.append(word_to_score(word))
    index_best_word=scores.index(max(scores))
    return list_of_words[index_best_word]
        
