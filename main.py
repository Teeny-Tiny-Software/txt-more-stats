from collections import Counter
import re
import os

def count_words(file_path):
    if not os.path.exists(file_path) or not file_path.endswith('.txt'):
        print("File does not exist or is not a text file.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_count = Counter(words)

    return word_count

def main():
    file_path = input("Enter the path to the text file: ")
    word_count = count_words(file_path)

    if word_count:
        print("\nWord Frequency Count:")
        for word, count in word_count.most_common():
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
