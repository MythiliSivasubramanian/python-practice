def word_frequency(sentence):
    """Return a dictionary with word counts."""
    freq = {}
    words = sentence.lower().split()

    for w in words:
        freq[w] = freq.get(w, 0) + 1

    return freq

print(word_frequency("Python is easy and python is powerful"))
