import os.path


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    filename = os.path.basename(book_path)
    print(f"{filename} contais {count} words")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    """

    :type text: str
    """
    words = text.split()
    return len(words)


main()