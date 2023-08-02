class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        arr = []
        for row in nums:
            mx_heap = []
            for num in row:
                heappush(mx_heap, -num)
            arr.append(mx_heap)

        res = []
        for i in range(n):
            temp = -1
            for j in range(m):
                temp = max(temp, -heappop(arr[j]))
            res.append(temp)

        return sum(res)
        