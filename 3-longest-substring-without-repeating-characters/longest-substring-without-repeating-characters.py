class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
         
        return longest 

        