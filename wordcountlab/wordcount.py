import string
import re
from collections import Counter

# Function definitions
def count_specific_word(text, word):
    """Count the number of occurrences of a specific word in the text."""
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return words.count(word.lower())

def most_common_word(text):
    """Identify the most common word in the text."""
    if not text.strip():
        return ("None", 0)  # Handle empty input gracefully
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

def average_word_length(text):
    """Calculate the average length of words in the text, excluding punctuation."""
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)

def count_paragraphs(text):
    """Count the number of paragraphs in the text."""
    paragraphs = [para for para in text.split("\n\n") if para.strip()]
    return len(paragraphs)

def count_sentences(text):
    """Count the number of sentences in the text."""
    sentences = re.split(r'[.!?]', text)
    return len([s for s in sentences if s.strip()])

def show_menu():
    """Display the menu of options."""
    print("\nWhat would you like to do?")
    print("1. Count a specific word")
    print("2. Find the most common word")
    print("3. Calculate the average word length")
    print("4. Count the number of paragraphs")
    print("5. Count the number of sentences")
    print("6. Exit")

# Main function to implement the menu-based interaction
def main():
    file_path = 'News Article for Python Assessment.txt'  # Path to the text file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path.")
        return

    print("\nWelcome to the Text Analysis Tool!")
    print("This tool lets you analyze your text file with various options.")

    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            word = input("Enter the word you'd like to count: ").strip()
            count = count_specific_word(text, word)
            print(f"The word '{word}' appears {count} time(s) in the text.")
        elif choice == 2:
            common_word, frequency = most_common_word(text)
            print(f"The most common word is '{common_word}', which appears {frequency} time(s).")
        elif choice == 3:
            avg_length = average_word_length(text)
            print(f"The average word length in the text is {avg_length:.2f} characters.")
        elif choice == 4:
            paragraphs = count_paragraphs(text)
            print(f"There are {paragraphs} paragraph(s) in the text.")
        elif choice == 5:
            sentences = count_sentences(text)
            print(f"There are {sentences} sentence(s) in the text.")
        elif choice == 6:
            print("Exiting the Text Analysis Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()