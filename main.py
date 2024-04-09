def main():
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    count_words = get_num_words(text)
    counter_letters = count_letter(text)
    char_list = dict_to_list(counter_letters)
    char_list.sort(reverse=True, key=sort_on)
    
    #printing the report of the text
    print(f"The number of words is {count_words}")
    for element in char_list:
        print(f"The '{element['name']}' character was found '{element['num']}'")
    
#changing dictinary to list of dictinaries
def dict_to_list(dict):
    list = []

    for element in dict:
        if element.isalpha():
            list.append({"name": element, "num": dict[element]})

    return list

#showing sort function where to sort
def sort_on(dict):
    return dict["num"]

#opening the file and reading its content
def open_file(path):
    with open(path) as f:
        return f.read()

#couting the letters in text
def count_letter(text):
    counter_letter = {}
    lowered_text = text.lower()
    chars = list(lowered_text)

    for char in chars:
        if char not in counter_letter:
            counter_letter[char] = 1
        else:
            counter_letter[char] += 1

    return counter_letter

#getting the number of words from list
def get_num_words(text):
    words = text.split()
    return len(words)

main()
