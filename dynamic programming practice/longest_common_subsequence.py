n = input("Please enter first string: ")
n = list(n)
k = input("Please enter second string: ")
k = list(k)

cache = [[-1 for x in range(len(k))] for x in range(len(n))]
subs = ""

def subseq(i,j): 
  global subs
  if (i<0):
     return 0
  if (j<0):
    return 0
  if (i<0 | j<0):
    return 0
  elif cache[i][j]!=-1:
    return cache[i][j]
  elif n[i] == k[j]:
    subs+=n[i]
    res = 1 + subseq(i-1,j-1)
    cache[i][j] = res
    return res
  else:
    res = max(subseq(i-1,j),subseq(i,j-1))
    cache[i][j] = res
    return res

print("length of LCS is " + str(subseq(len(n)-1,len(k)-1)))
print("subsequence is: " + subs[::-1])