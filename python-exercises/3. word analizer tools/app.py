text = "Hello hello world! Python is fun, and Python is powerful."


# ✅ Features to Implement:
# Take a sentence from the user.

# Count the number of words.

# Print the longest word.

# Count how many times each word appears (word frequency).

# Remove punctuation and make it case-insensitive.
 
print(f"the total words is {len(text)}")
print(f"the longest word is {max(text.split(), key=len)}")

# word frequency
words = text.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# print
for word, count in word_count.items():
    print(f"{word}: {count}")
