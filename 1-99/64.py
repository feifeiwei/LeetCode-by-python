'''
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

'''
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        dp = grid
        
        for i in range(m):
            for j in range(n):
                
                if i==0 and j ==0:
                    dp[i][j] = grid[i][j]
                    
                elif i==0 and j > 0:
                    dp[i][j] = grid[i][j] + grid[i][j-1]
                
                elif i > 0 and j == 0:
                    dp[i][j] = grid[i][j] + grid[i-1][j]
                
                elif i > 0 and j > 0:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]
      
      
      
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        dp = grid
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i==m-1 and j == n-1):
                    dp[i][j] = grid[i][j]
                elif (i==m-1 and j <n-1):
                    dp[i][j] = grid[i][j]+grid[i][j+1]
                elif (i<m-1 and j==n-1):
                    dp[i][j] = grid[i][j]+grid[i+1][j]
                elif (i<m-1 and j<n-1):
                    dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
        print(dp)
        return dp[0][0]
