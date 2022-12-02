class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 10**9+7
        sums = 0
        arr.append(0) #Sentinel value to pop all elements off the stack
        stack = [-1]
        
#         [3, 1, 2, 4, 0]
#         
#         [-1]   index = 1    i1 = -1   lef = 2   rig = 3     
#         idx = -1
        
        for i2,num in enumerate(arr):
	      #Mantain a monotone increasing stack
            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]   # First lesser element to the left
                left = index-i1
                right = i2-index
                sums += right*left*arr[index]
            stack.append(i2)
            
        return sums%M
        