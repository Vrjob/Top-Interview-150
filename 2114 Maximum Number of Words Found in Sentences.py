"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
"""
def mostWordsFound1(self, sentences):
    listNew = []

    for i in sentences:
        count = 1

        for j in i:
            if j in " ":
                count += 1

        listNew.append(count)
    return max(listNew)

def mostWordsFound2(self, sentences):
    max_words = 0

    for sentence in sentences:
        words = sentence.split()  
        word_count = len(words)  

        if word_count > max_words:
            max_words = word_count
            
    return max_words