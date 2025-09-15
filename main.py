from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

main()
