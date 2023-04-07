class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        look_up = Counter(banned)
        cnt, curSum = 0, 0        
        
        for i in range(1, n + 1):
            if i in look_up:
                continue 
                
            curSum += i
            if curSum > maxSum:
                break
            else:
                cnt += 1
                
        return cnt 
        