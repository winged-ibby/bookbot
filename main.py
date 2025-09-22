import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    dicts_list = get_dicts_list(num_chars)
    sorted_list = sort_dicts_list(dicts_list)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
