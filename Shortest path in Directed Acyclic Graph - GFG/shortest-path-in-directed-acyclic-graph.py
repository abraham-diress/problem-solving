#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
            
        #Build our adj list 
        #We get the topo sort
        #Build the answer
        
        #adjList[u]: {v, wt}
        
        adjList = [[] for _ in range(n)]
        
        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            adjList[u].append([v, wt])
        
        stack = []
        visit = [0] * n
        
        for i in range(n):
            if not visit[i]:
                self.topoSort(i, adjList, visit, stack)
                
        dist = [float('inf')] * n 
        dist[0] = 0
        
        while stack:
            node = stack.pop()
            
            for child in adjList[node]:
                v = child[0]
                wt = child[1]
                if dist[node] + wt < dist[v]:
                    dist[v] = dist[node] + wt
        
        for i in range(len(dist)):
            if dist[i] == float('inf'):
                dist[i] = -1
            
        return dist
        
    def topoSort(self, node, adjList, visit, stack):
        visit[node] = 1
        
        for child in adjList[node]:
            childNode = child[0]
            if visit[childNode] == 0:
                self.topoSort(childNode, adjList, visit, stack)

        stack.append(node)
            
        
        
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends