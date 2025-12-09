from operator import le
import sys
from stats import num_of_words , num_of_characters, sort_char

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_p = ""
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_p = sys.argv[1]

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(get_book_text(file_p))} total words")
    print("---------- Character Count -------")
    sorted_chars = sort_char(num_of_characters(get_book_text(file_p)))
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        # 3. skip non-letters
        if not ch.isalpha():
            continue
        print(f"{ch}: {num}")
main()