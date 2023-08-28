def find_and_replace_pattern(words, pattern):
    pattern_steps = []

    for i, char in enumerate(pattern, 1):
        difference = ord(char) - ord(pattern[i-1])
        pattern_steps.append(difference)
    
    for word in words:
        word_steps = []

        for i, char in enumerate(word, 1):
            difference = ord(char) - ord(word[i-1])
            word_steps.append(difference)

        if word_steps != pattern_steps:
            words.remove(word)

    return words
        
