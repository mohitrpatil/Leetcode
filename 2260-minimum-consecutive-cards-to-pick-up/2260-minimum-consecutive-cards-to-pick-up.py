class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        pos = defaultdict(list)
        
        for i, nums in enumerate(cards):
            pos[nums].append(i)

        mini = 99999999
        
        
        for key, value in pos.items():
            if len(value)>1:
                local_mini = 9999999
                for i in range(1,len(value)):
                    local_mini = min(local_mini, value[i]-value[i-1]+1)
                mini = min(mini,local_mini)
                
        if mini != 99999999:
            return mini
        else:
            return -1
