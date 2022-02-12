def words_check(text):
    words = text.lower().split()
    dictionary = {}
    for word in words:
        clean_word = word
        for c in word:
            if c not in 'abcdefghijklmnopqrstuvwxyz':
                clean_word = clean_word.replace(c, '', 1)
        if len(clean_word) > len(word)//2:
            clean_word = clean_word.capitalize()
            if clean_word in dictionary:
                dictionary[clean_word] += 1
            else:
                dictionary[clean_word] = 1
    return dictionary
