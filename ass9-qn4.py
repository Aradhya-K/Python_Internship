def word_length_dict(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}

sentence = input("enter a sentence: ")

word_lengths = word_length_dict(sentence)

print(word_lengths)