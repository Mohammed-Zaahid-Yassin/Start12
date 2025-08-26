import random
words = ["python", "program", "karnataka", "laptop", "security", "science", "engineer", "hardware", "project", "formula"]
word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))
print("Word Scramble Game!")
print(f"Scrambled word: {scrambled}")
guess = input("Guess the original word: ")
if guess.lower() == word:
    print("Correct! Well done.")
else:
    print(f"Incorrect. The word was: {word}")
