class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = [False] * 128
        dic = Counter(s)
        
        for ch in s:
            dic[ch] -= 1
            while stack and seen[ord(ch)] == False and ch < stack[-1] and dic[stack[-1]] > 0:
                seen[ord(stack.pop())] = False
            if seen[ord(ch)] == False:
                stack.append(ch)
                seen[ord(ch)] = True
        return ''.join(stack)
        
        