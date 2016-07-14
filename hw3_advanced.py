import re

my_reversed_list = []

def is_palindrome(sentence):
    length = len(sentence)

    for item in sentence:
        my_reversed_list.append(sentence[length-1])
        length -= 1

    print(sentence)
    print(my_reversed_list)

    if sentence == my_reversed_list:
        print("Your sentence is a palindrome")
    else:
        print("Your sentence is not a palindrome")


def main():
    sentence = input("Please input a word/sentence: ").lower()
    characters_only = re.sub("[^A-Za-z0-9]", "", sentence)
    print("Your sentence without the special characters is: ", characters_only)
    sentence = list(characters_only)

    is_palindrome(sentence)

if __name__ == '__main__':
    main()
