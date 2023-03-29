class Solution:
    def swap(self, mp, ch1, ch2): 
        mp[ch1]+=1
        mp[ch2]-=1
        
        if(mp[ch2]==0):
            del mp[ch2] 
        
        
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        mp1, mp2 = Counter(word1), Counter(word2)
	
		
        for c1 in string.ascii_lowercase:        
            for c2 in string.ascii_lowercase:     
                
                if c1 not in mp1 or c2 not in mp2:  
                    continue

                self.swap(mp1, c2, c1) 
                self.swap(mp2, c1, c2)
                
                if len(mp1)== len(mp2):  
                    return True
				
                self.swap(mp1, c1, c2) 
                self.swap(mp2, c2, c1)
                
        return False
        