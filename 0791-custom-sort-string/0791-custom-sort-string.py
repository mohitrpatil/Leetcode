class Solution:
    def customSortString(self, order: str, s: str) -> str:

        count = Counter(s)
        ans = ""

        for i in range(len(order)):
            if order[i] in count.keys():
                ans += order[i] * count[order[i]]
                count[order[i]] = 0

        for key, value in count.items():
            if value >0:
                ans += key * count[key]

        return ans