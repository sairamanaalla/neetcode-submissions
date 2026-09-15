class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        ans = 0
        left = 0

        for i in range(len(s)):

            while s[i] in window:
                window.remove(s[left])
                left += 1

            window.add(s[i])

            ans = max(ans, len(window))

        return ans

        