def solve(A, B):
  ans=0
  i=len(A)
  j=len(B)
  dp=[[-1]*i for _ in range(j)]
  def lcs(A,B,i,j):
      if i<0 or j<0:
          return 0
      if dp[i][j]!=-1:
          return dp[i][j]
      if A[i]==B[j]:
          ans=lcs(A,B,i-1,j-1)+1
      else:
          ans=max(lcs(A,B,i-1,j),lcs(A,B,i,j-1))
      dp[i][j]=ans
      return ans
  return lcs(A,B,i-1,j-1)


A = "abbcdgf"
B = "bbadcgf"
print(solve(A,B))

# output:
# 5

# longest common subsequence is "bbcgf"