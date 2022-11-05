class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        inDegree = [0] * numCourses 
        
        for course, pre in prerequisites:
            adjList[pre].append(course)
            inDegree[course] += 1
        
        q = deque()
        
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)
                
        coursesTaken = 0
        while q:
            cur = q.popleft()
            coursesTaken += 1
            
            for node in adjList[cur]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    q.append(node)
                    
        return coursesTaken == numCourses
                
            
            
        
            
         