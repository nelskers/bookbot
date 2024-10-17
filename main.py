def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)
    count_words(file_contents)

    characters = count_chars(file_contents)
    sorted_chars = sorted_characters(characters)

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

def count_words(text):
    words = text.split()
    word_count = len(words)
    print(f"Word Count: {word_count}")

def count_chars(text):
    lower_string = text.lower()
    characters = {}


    for character in lower_string:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1

    return characters

def sorted_characters(characters):
    # Convert dictionary to a list of tuples (character, frequency)
    char_list = [(char, count) for char, count in characters.items() if char.isalpha()]

    # Sort the list by frequency in descending order
    char_list.sort(key=lambda x: x[1], reverse=True)

    return char_list
if __name__ == "__main__":
    main()
    
