class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        w = len(words)
        string = ""
        for i in range(w):
            string = string+words[i]
        
        d = Counter(string)
        for key, values in d.items():
            if values % w != 0:
                return False
        return True