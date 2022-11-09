class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxSoFar = -1
        
        for i in range(len(arr) - 1, -1, -1):
            curMax = max(maxSoFar, arr[i])
            arr[i] = maxSoFar
            maxSoFar = curMax
        return arr
            
    
        
        