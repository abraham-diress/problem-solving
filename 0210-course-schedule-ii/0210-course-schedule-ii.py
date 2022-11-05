class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        inDegree = [0] * numCourses 
        ans = []
        
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
            ans.append(cur)
            coursesTaken += 1
            
            for node in adjList[cur]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    q.append(node)
                    
        return ans if len(ans) == numCourses else []
        