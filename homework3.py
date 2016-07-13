import re

my_second_list = []

def is_polindrome(sentence):
    if sentence == []:
        return

    is_polindrome(sentence[1:])
    my_second_list.append(sentence[0])

def main():
    sentence = input("Please input a word/sentence: ").lower()
    characters_only = re.sub("[^A-Za-z0-9]", "", sentence)
    print("Your sentence without the special characters is: ", characters_only)
    sentence = list(characters_only)

    is_polindrome(sentence)
    # if is_polindrome(sentence):
    #     print("Your sentence is a palindrome")
    # else:
    #     print("Your sentence is not a palindrome")

    print(sentence)
    print(my_second_list)

    if sentence == my_second_list:
        print("Your sentence is a palindrome")
    else:
        print("Your sentence is not a palindrome")

if __name__ == '__main__':
    main()
