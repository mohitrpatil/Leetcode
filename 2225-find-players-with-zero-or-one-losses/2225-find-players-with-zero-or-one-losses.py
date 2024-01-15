class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        tally = defaultdict(list)
        s = set()
        for i  in range(len(matches)):
            for j in range(2):
                s.add(matches[i][j])

        for x in s:
            tally[x] = [0,0]
        
        for match in matches:
            tally[match[0]][0] +=1
            tally[match[1]][1] +=1

        answer1 = []
        answer2 = []
        for key, value in tally.items():
            if value[1] == 0:
                answer1.append(key)
            if value[1] == 1:
                answer2.append(key)


        return [sorted(answer1) , sorted(answer2)]
                
                
        