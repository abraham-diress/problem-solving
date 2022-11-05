class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 - white, 1 - grey, 2 - black
        status = [0] * numCourses 
        adjList = [[] for _ in range(numCourses)]
        
        for course, pre in prerequisites:
            adjList[pre].append(course)
            
        def dfs(node):
            if status[node] == 1:
                return False 
            if status[node] == 2:
                return True
            
            status[node] = 1
            for child in adjList[node]:
                if not dfs(child):
                    return False
            status[node] = 2
            
            return True
            
        for i in range(numCourses):
            if status[i] == 0:
                if not dfs(i):
                    return False
                
        return True
            
            
    
        
        
        
                
            
            
        
            
         