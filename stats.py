from curses.ascii import isalpha


def num_of_words(book_text):
    words = book_text.split()
    return len(words)

def num_of_characters(book_text):
    num_dict = {}
    book_text_lower = book_text.lower()
    for char in book_text_lower:
        if char.isalpha():
            if char in num_dict:
                num_dict[char] += 1
            else:
                num_dict[char] = 1
    return num_dict

def sort_on_num(item):
    return item["num"]

def sort_char(char_dict):
    sort_list = []
    
    for key, value in char_dict.items():
        small_dict = {
            "char": key,
            "num": value
        }

        sort_list.append(small_dict)

    sort_list.sort(reverse=True, key=sort_on_num)
    return sort_list