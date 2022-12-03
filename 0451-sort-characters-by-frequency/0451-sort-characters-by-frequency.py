class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count = sorted(count.items(), key=lambda item: item[1], reverse = True)
        ans = ''
        
        for ch in count:
            freq = ch[1]
            for _ in range(freq):
                ans += ch[0]
            
        return ans 
        