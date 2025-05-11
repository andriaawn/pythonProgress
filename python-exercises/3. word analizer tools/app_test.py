
text = "in this world, only the strong people can be survive"

# count the number 

words = text.split()

print(f"total words in text is {len(words)}")

print(f"the longest word is {max(words, key=len)}")


word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for word, count in word_freq.items():
    print(f"{word, count}")