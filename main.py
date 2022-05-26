# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    word1.lower()
    word2.lower()
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

# print(find_anagrams('listen', 'silent'))
print(find_anagrams(input('Type a word that is an anagram: \n'), input('Type a word that is an anagram of the first word: \n')))