def reverse_words_in_place(sentence):
    words = sentence.split()
    print(words)
    reversed_list = []
    for word in words:
        reversed_list.append(word[::-1])
    print(reversed_list)
    reversed_sentence = " ".join(reversed_list)
    print(reversed_sentence)


reverse_words_in_place("I am not a straight sentence")

