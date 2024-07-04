class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans = []

        sorted_arr = sorted(nums)
        
        for i in range(int(len(sorted_arr)/2)):
            s = (sorted_arr[i] + sorted_arr[-i-1]) / 2
            ans.append(s)

        return min(ans)