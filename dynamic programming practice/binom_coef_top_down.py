#quick and dirty top down binomial coefficient

n = int(input("Please enter n: "))
k = int(input("Please enter k: "))

cache = [[-1 for x in range(k+1)] for x in range(n+1)]

def binomco(i,j):
  if (i < j):
    return 0;
  elif (j==1):
    return i
  elif (i==j):
    return 1
  else:
    if cache[i][j] != -1:
      return cache[i][j]
    else:
      res= binomco(i-1,j-1)+binomco(i-1,j)
      cache[i][j] = res
      return res
      

print("Result: " + str(binomco(n,k)))