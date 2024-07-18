def count_words(sentence):
    words = sentence.split()

    words_freq = {}

    for word in words:

        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1
    print("word frequencies:")

    for word, freq in words_freq.items():
        print(f"{word} : {freq}")

sentence = "i want to go home"

count_words(sentence)