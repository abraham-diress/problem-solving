class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        gains = sorted([a - b for (a, b) in zip(reward1, reward2)])
        return sum(reward2) + sum(gains[n - k:])
        