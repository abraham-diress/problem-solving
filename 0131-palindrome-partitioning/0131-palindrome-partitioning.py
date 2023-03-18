class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = [] 
        path = [] 

        def helper(i):
            if i == len(s):
                ans.append(path.copy())
                return 

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    path.append(s[i:j+1])
                    helper(j + 1)
                    path.pop()

        helper(0)
        return ans
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
