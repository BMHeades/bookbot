from stats import get_book_text, get_num_words, get_char_count, split_char_and_count, sort_by_value

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book_text)
    # print(f"{num_words} words found in the document")
    chars_dict = get_char_count(book_text)
    chars_list = split_char_and_count(chars_dict)
    sorted_list = sort_by_value(chars_list)
    # print(sorted_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

main()