class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #Time complexity: O(N) - N: 1001
        arr = [0] * 1001

        for trip in trips:
            start = trip[1]
            end = trip[2]

            arr[start] += trip[0]
            arr[end] -= trip[0]
        
        compute = capacity
        i = 0
        while i < 1001 and compute >= 0:
            compute -= arr[i]
            i += 1
        
        return compute >= 0
