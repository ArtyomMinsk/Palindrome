import re

my_reversed_list = []

def is_palindrome(sentence):
    my_reversed_list = []
    characters_only = re.sub("[^A-Za-z0-9]", "", sentence).lower()
    print("Your sentence without the special characters is: ", characters_only)
    sentence = list(characters_only)

    length = len(sentence)

    for item in sentence:
        my_reversed_list.append(sentence[length-1])
        length -= 1

    print(sentence)
    print(my_reversed_list)

    if sentence == my_reversed_list:
        print("Your sentence is a palindrome")
        return True
    else:
        print("Your sentence is not a palindrome")
        return False


def main():
    sentence = input("Please input a word/sentence: ")

    is_palindrome(sentence)

if __name__ == '__main__':
    main()
