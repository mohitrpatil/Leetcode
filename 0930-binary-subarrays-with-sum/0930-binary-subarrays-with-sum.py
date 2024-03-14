class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def sliding(target):
            left_pointer = current_sum = ans = 0

            for right_pointer in range(len(nums)):
                current_sum += nums[right_pointer]
                while current_sum > target and left_pointer <= right_pointer:
                    current_sum -= nums[left_pointer]
                    left_pointer += 1
                ans += right_pointer - left_pointer + 1
            return ans

        return sliding(goal) - sliding(goal - 1)