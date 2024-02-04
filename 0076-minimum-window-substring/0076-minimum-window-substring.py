
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        char_frequency_t = defaultdict(int)
        for char in t:
            char_frequency_t[char] += 1

        left = 0
        min_len = float('inf')
        min_left = 0
        count = len(t)

        for right in range(len(s)):
            current_char = s[right]

            if current_char in char_frequency_t:
                char_frequency_t[current_char] -= 1
                if char_frequency_t[current_char] >= 0:
                    count -= 1

            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                left_char = s[left]
                if left_char in char_frequency_t:
                    char_frequency_t[left_char] += 1
                    if char_frequency_t[left_char] > 0:
                        count += 1
                left += 1

        return "" if min_len == float('inf') else s[min_left:min_left + min_len]