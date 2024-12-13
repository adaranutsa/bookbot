def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    word_count_list = []
    for key, value in char_count.items():
        word_count_list.append({"char": key, "count": value})

    word_count_list.sort(reverse=True, key=sort_on)
    
    for item in word_count_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")

main()