print("=== Word Frequency Counter ===")

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print("\nWord Frequency:")
for word, count in freq.items():
    print(f"{word}: {count}")
