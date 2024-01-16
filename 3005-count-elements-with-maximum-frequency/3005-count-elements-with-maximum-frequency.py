class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        dict1 = Counter(nums)
        print(dict1)
        # sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_dict)

        count = 0
        
        max_value = max(dict1.values())
        print(max_value)

        for key, value in dict1.items():
            
            if max_value == value:
                count += value

                
        return count