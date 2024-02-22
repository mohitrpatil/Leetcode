class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if (len(trust) == 0 and n ==1):
            return 1

        people_trusting = []
        t = defaultdict(set)

        for i in range(len(trust)):
            people_trusting.append(trust[i][0])

        for i in range(len(trust)):
            t[trust[i][1]].add(trust[i][0])

        for key, value in t.items():
            if len(value) == n-1:
                if key not in people_trusting:
                    return key
        
        return -1
        