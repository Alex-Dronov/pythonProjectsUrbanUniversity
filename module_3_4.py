def single_root_words(root_word, *other_words):
    same_words = []
    root_word = str(root_word).lower()

    for i in other_words:
        i = str(i)
        test_word = i.lower()

        if (root_word in test_word) or (test_word in root_word):
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)