class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = [] 
        digit = [] 

        for log in logs:
            if log[-1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter_ = [] 

        for log in letter:
            idx = log.index(" ")
            tmp = log[idx + 1:]
            letter_.append((tmp, log[:idx]))
        
        letter_.sort()

        ans = [] 
        for letter in letter_:
            ans.append(letter[1] + " " + letter[0])
        
        ans.extend(digit)

        return ans 







            
                



        

            
        




