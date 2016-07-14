import re

my_reversed_list = []

def is_palindrome(sentence):
    characters_only = re.sub("[^A-Za-z0-9]", "", sentence).lower() #removes special characters
    print("Your sentence without the special characters is: ", characters_only)

    sentence = list(characters_only)
    print(sentence)

    reverse_list(sentence)
    print(my_reversed_list)

    if sentence == my_reversed_list:
        print("Your sentence is a palindrome!")
        return True
    else:
        print("Your sentence is not a palindrome!")
        return False

def reverse_list(sentence):
    if sentence == []:
        return True

    reverse_list(sentence[1:])
    my_reversed_list.append(sentence[0])

def main():
    sentence = input("Please input a word/sentence: ")

    is_palindrome(sentence)

if __name__ == '__main__':
    main()
