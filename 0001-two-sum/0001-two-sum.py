class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        ans = []
        for i in range (len(nums)):
            if target - nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                ans.append(i)
                ans.append(hashmap[target - nums[i]])
        
        return ans

        
