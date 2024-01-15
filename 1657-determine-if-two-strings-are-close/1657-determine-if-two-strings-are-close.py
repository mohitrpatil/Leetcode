class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        count_word1 = Counter(word1)
        count_word2 = Counter(word2)

        if len(word1)!=len(word2):
            return False
        elif count_word1 == count_word2:
            return True
        else:
            if count_word1.keys() == count_word2.keys():
                if sorted(count_word1.values()) == sorted(count_word2.values()):
                    return True
                else:
                    return False
            else:
                return False