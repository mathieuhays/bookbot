import os.path


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    filename = os.path.basename(book_path)
    stat = get_letter_stats(text)

    print(f"{filename} contains {count} words")
    print("Letter stats:")
    print(stat)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_letter_stats(text: str) -> object:
    stats = {}

    for char in text.lower():
        if char.isalpha():
            if char in stats:
                stats[char] += 1
            else:
                stats[char] = 1

    return stats


main()
