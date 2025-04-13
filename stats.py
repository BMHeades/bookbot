def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def get_char_count(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def split_char_and_count(dict):
    new_list = []
    for key in dict:
        if key.isalpha():
            new_dict = {}
            new_dict["char"] = key
            new_dict["count"] = dict[key]
            new_list.append(new_dict)

    return new_list

def sort_on(dict):
    return dict["count"]

def sort_by_value(list):
    new_list = list
    new_list.sort(reverse=True, key=sort_on)
    return new_list