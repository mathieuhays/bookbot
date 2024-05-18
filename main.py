import os.path


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    filename = os.path.basename(book_path)
    stat = get_letter_stats(text)
    stat_list = process_letter_stats(stat)

    print("[  === BOOK REPORT ===  ]")
    print(f"{filename} contains {count} words\n")
    print("Letter statistics -------")

    render_stats(stat_list)
    print("[  ======= END =======  ]")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_letter_stats(text: str) -> dict:
    stats = {}

    for char in text.lower():
        if char.isalpha():
            if char in stats:
                stats[char] += 1
            else:
                stats[char] = 1

    return stats


def stat_sort_on(obj: dict) -> int:
    return obj["count"]


def process_letter_stats(stats: dict) -> list:
    stat_list = []

    for letter in stats:
        stat_list.append({
            "letter": letter,
            "count": stats[letter]
        })

    stat_list.sort(reverse=True, key=stat_sort_on)

    return stat_list


def render_stats(stat_list: [dict]):
    for stat in stat_list:
        print(f"The '{stat['letter']}' character was found {stat['count']} times")


main()
