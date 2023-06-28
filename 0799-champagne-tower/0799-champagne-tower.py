class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cups = [[0.0 for _ in range(101)] for _ in range(101)]
        cups[0][0] = poured 
        
        for i in range(100):
            for j in range(i + 1):
                if cups[i][j] >= 1:
                    cups[i + 1][j] += (cups[i][j] - 1) / 2
                    cups[i + 1][j + 1] += (cups[i][j] - 1) / 2
                    cups[i][j] = 1
        
        return cups[query_row][query_glass]
                    
    
        