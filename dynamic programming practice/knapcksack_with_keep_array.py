n = 5
w = [1,2,2,2,2]
c = [1,2,3,4,5]

#max weight
max_w = 4;

#array to memoize
v = [[0 for x in range(max_w+1)] for x in range(n+1)]
#keep array
keep = [[False for x in range(max_w+1)] for x in range(n+1)];

def knapsack(max_w):
  for i in range(0,n):
    for k in range(0,max_w+1):
      if i == 0 | k == 0:
        v[i][k] = 0;
      elif w[i] <= k:
        v[i][k] = max(c[i] + v[i-1][k-w[i]], v[i-1][k])
        keep[i][k] = True
      else:
        v[i][k] = v[i-1][k]
      

knapsack(max_w)
print("Done.")
print("The solution to max weight "+str(max_w)+" is: " + str(v[n-1][max_w]))

#print pairs
print("Included items")
ck = max_w
for m in range(n-1,-1,-1):
  if keep[m][ck]:
	  print("item "+str(m)+", weight "+str(w[m])+" and value "+str(c[m]))
	  ck-=w[m]