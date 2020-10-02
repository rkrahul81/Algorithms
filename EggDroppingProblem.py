#Egg Dropping Memoization
f = 15
e = 3
dp = [[-1 for x in range(f+1)]for x in range(e+1)] 
def eggdrop(f,e):
  if dp[e][f]!=-1:
    return dp[e][f]
  if f==0 or f==1:
    return f
  if e==1:
    return f
  mn = 10**9
  ans = 0
  for k in range(1,f+1):
    temp =  1 + max(eggdrop(k-1,e-1),eggdrop(f-k,e))
    mn = min(temp,mn)
  dp[e][f] = mn
  return mn

print(eggdrop(f,e))
