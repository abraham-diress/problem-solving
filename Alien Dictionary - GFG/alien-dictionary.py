#User function Template for python3
from collections import deque
class Solution:
    def findOrder(self,dict, N, K):

        def topoSort(v, adjList):
            inDegree = [0] * K
            
            for i in range(K):
                for ch in adjList[i]:
                    inDegree[ch] += 1
            
            q = deque()
            for i in range(len(inDegree)):
                if inDegree[i] == 0:
                    q.append(i)
                    
            topo = [] 
            
            while q:
                node = q.popleft()
                topo.append(node)
                
                for ch in adjList[node]:
                    inDegree[ch] -= 1
                    if inDegree[ch] == 0:
                        q.append(ch)
            return topo
  
        adjList = [[] for _ in range(K)]
        
        for i in range(N - 1):
            st1 = dict[i]
            st2 = dict[i + 1]
            size = min(len(st1), len(st2))
            
            for ptr in range(size):
                if st1[ptr] != st2[ptr]:
                    adjList[ord(st1[ptr]) - ord('a')].append(ord(st2[ptr]) - ord('a'))
                    break
                
        topo = topoSort(K, adjList)
        ans = ""
        
        for ch in topo:
            ans += chr(ch + ord('a'))
     
        return ans 
            
                
        #Topological sort 
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends