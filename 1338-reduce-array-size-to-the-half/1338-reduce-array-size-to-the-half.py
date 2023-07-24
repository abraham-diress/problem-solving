class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = Counter(arr)
        frequencies = list(cnt.values())
        frequencies.sort()
        
        ans, removed, half = 0, 0, len(arr) // 2
        while removed < half:
            ans += 1
            removed += frequencies.pop()
        return ans
        
        