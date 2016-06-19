def word_count(string):
    word_count = {}
    string = string.lower().split(" ")

    for word in string:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

print(word_count("Olly oLLY cOME IN FREE"))
