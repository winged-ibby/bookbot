from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    dicts_list = get_dicts_list(num_chars)
    sorted_list = sort_dicts_list(dicts_list)
    
    print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {filepath}...
        ------------ Word Count ------------
        Found {num_words} total words
        ------------ Character Count ------------
        {sorted_list}
        ============ END ============
    """)

main()
