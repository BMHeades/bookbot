import sys
from stats import get_book_text, get_num_words, get_char_count, split_char_and_count, sort_by_value

def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = arguments[1]


    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    # print(f"{num_words} words found in the document")
    chars_dict = get_char_count(book_text)
    chars_list = split_char_and_count(chars_dict)
    sorted_list = sort_by_value(chars_list)
    # print(sorted_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")
    

main()