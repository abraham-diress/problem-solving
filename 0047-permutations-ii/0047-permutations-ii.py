class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        count = Counter(nums)
        
        self.dfs([], res, count, nums)
        return res 
        
    def dfs(self, perms, res, count, nums):
        if len(perms) == len(nums):
            res.append(perms.copy())
            return 
        
        for n in count:
            if count[n] >= 1:
                perms.append(n)
                count[n] -= 1
                
                self.dfs(perms, res, count, nums)
                
                perms.pop()
                count[n] += 1
    
        