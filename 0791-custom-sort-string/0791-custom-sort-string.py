class Solution:
    def customSortString(self, order: str, s: str) -> str:

        count = Counter(s)
        ans = ""

        for i in range(len(order)):
            x = order[i]
            if x in count.keys():
                for i in range(count[x]):
                    ans += x
                count[x] = 0

        for key, value in count.items():
            if value >0:
                for i in range(count[key]):
                    ans += key

        return ans