CHECK_WORD_1 = "TRUE"
CHECK_WORD_2 = "LOVE"


def calculate_common_letters(name, checked_word):
    name = name.upper()
    checked_word = checked_word.upper()
    checked_letters = list(checked_word)
    result = {}

    for letter in checked_letters:
        result[letter] = name.count(letter)

    return result


def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()

    combined_names_word1 = calculate_common_letters(combined_names, CHECK_WORD_1)
    combined_names_word2 = calculate_common_letters(combined_names, CHECK_WORD_2)

    word1_total = sum(combined_names_word1.values())
    word2_total = sum(combined_names_word2.values())

    love_score = str(word1_total) + str(word2_total)

    print(love_score)


name1 = input("Name1: ")
name2 = input("Name2: ")

calculate_love_score(name1, name2)
