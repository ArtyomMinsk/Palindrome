import re

def is_palindrome(sentence):
    my_reversed_list = []
    characters_only = re.sub("[^A-Za-z0-9]", "", sentence).lower() #removes special characters
    # print("Your sentence without the special characters is: ", characters_only)

    sentence = list(characters_only)
    # print(sentence)

    reverse_list(sentence, my_reversed_list)
    # print(my_reversed_list)

    if sentence == my_reversed_list:
        return True
    else:
        return False

def reverse_list(sentence, my_reversed_list):
    if sentence == []:
        return True
    reverse_list(sentence[1:], my_reversed_list)
    my_reversed_list.append(sentence[0])

def main():
    sentence = input("Please input a word/sentence: ")

    if is_palindrome(sentence):
        print("Your sentence is a palindrome!")
    else:
        print("Your sentence is not a palindrome!")

if __name__ == '__main__':
    main()
