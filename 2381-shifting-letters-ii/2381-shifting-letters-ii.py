class Solution:
    def shift(self, c, shift):
        return chr(((ord(c) - 97 + shift) % 26) + 97)   

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * (n + 1) 
        ans = ''
        
        for start, end, dir in shifts:
            if dir == 0:
                arr[start] -= 1
                arr[end + 1] += 1
            else:
                arr[start] += 1
                arr[end + 1] -= 1
        
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        for i in range(len(s)):
            ans += self.shift(s[i], arr[i]) 

        return ans 


        


            
