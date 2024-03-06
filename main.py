def main():
    path = "books/Frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    letter_nums = get_letter_counts(text)
    letter_nums_list = letter_counts_report(letter_nums)
    for letter in letter_nums_list:
        print(f"The {letter['letter']} character was found {letter['count']} times.")
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_letter_counts(text):
    letter_counts = {}
    lowered_text = text.lower()
    lowered_split_text = lowered_text.split()
    for words in lowered_split_text:
        for letter in words:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
    return letter_counts

def letter_counts_report(letter_counts):
    letter_counts_list = []
    for letter, count in letter_counts.items():
        if letter.isalpha():
            letter_counts_list.append({"letter": letter, "count": count})
    letter_counts_list.sort(reverse=True, key=sort_on)
    return letter_counts_list

def sort_on(dict):
    return dict["count"]



main()