def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    other_words_low = [word.lower() for word in other_words]

    for i in range(len(other_words_low)):
        if root_word in other_words_low[i]:
            same_words.append(other_words[i])

    for i in range(len(other_words_low)):
        if other_words_low[i] in root_word:
            same_words.append(other_words[i])

    # unique_same_words = []                    # если вдруг в списке попадется одинаковое c заданным слово -
    # for word in same_words:                   # удалит дубликат из-за срабатывания двух циклов for.
    #     if word not in unique_same_words:     # Единственный недостаток - если слово повторится во втором случае, то
    #         unique_same_words.append(word)    # оно останется на первом месте в списке, независимо, где оно было в списке

    return print(same_words)


single_root_words('Сад', 'Садовник', 'Сажать', 'посадка', 'рассада', 'Садовод',)
single_root_words('Международный', 'Народ', 'Междуречье', 'Род', 'Народная', 'рОД' ,'Родной',)
