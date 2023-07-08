def maxArea(A):
      p1=0
      p2=len(A)-1
      result=0
      while p1<p2:
          width=p2-p1
          mini=min(A[p1],A[p2])
          temp_ans=mini*width
          result=max(temp_ans,result)
          if A[p2]<A[p1]:
              p2-=1
          else:
              p1+=1
      return result


A = [1, 5, 4, 3]
print(maxArea(A))

# output:
# 6