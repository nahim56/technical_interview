# split string on spaces
# reverse words with more than 5 letters
# Spaces will be included only when more than one word is present.


def reverse_long_words(sentence: str) -> str:
    word_list = sentence.split(" ")
    res_word_list = []
    if len(word_list) == 1:
        if len(word_list[0]) >= 5:
            return word_list[0][::-1]
        else:
            return word_list[0]
    for word in word_list:
        if len(word) >= 5:
            res_word_list.append(word[::-1])
        else:
            res_word_list.append(word)
    return " ".join(res_word_list)


if __name__ == "__main__":
    pass
