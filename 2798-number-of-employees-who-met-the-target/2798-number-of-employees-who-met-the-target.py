class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        for hour in hours:
            if hour >= target:
                cnt += 1
        
        return cnt 
        