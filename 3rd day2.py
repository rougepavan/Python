def max_words_in_sentence(sentences):
    max_words = 0
    for sentence in sentences:
        words = sentence.split()
        max_words = max(max_words, len(words))
    return max_words
sentences1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
result1 = max_words_in_sentence(sentences1)
print(f"The maximum number of words in a single sentence is {result1}.")
sentences2 = ["please wait", "continue to fight", "continue to win"]
result2 = max_words_in_sentence(sentences2)
print(f"The maximum number of words in a single sentence is {result2}.")
