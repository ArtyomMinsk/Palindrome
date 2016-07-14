import re

my_reversed_list = []

def is_palindrome(sentence):
    if sentence == []:
        return True

    is_palindrome(sentence[1:])
    my_reversed_list.append(sentence[0])

def main():
    sentence = input("Please input a word/sentence: ").lower()
    characters_only = re.sub("[^A-Za-z0-9]", "", sentence) #removes special characters
    print("Your sentence without the special characters is: ", characters_only)
    sentence = list(characters_only)

    is_palindrome(sentence)

    print(sentence)
    print(my_reversed_list)

    if sentence == my_reversed_list:
        print("Your sentence is a palindrome!")
    else:
        print("Your sentence is not a palindrome!")

if __name__ == '__main__':
    main()
