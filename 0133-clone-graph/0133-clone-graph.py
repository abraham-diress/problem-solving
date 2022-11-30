"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        cloneMap = {}
        
        def clone(node):
            if node in cloneMap:
                return cloneMap[node]
            
            copy = Node(node.val)
            cloneMap[node] = copy 
            
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
                
            return copy
        
        return clone(node) if node else None
            

        