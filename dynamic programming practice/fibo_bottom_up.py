#quick and dirty bottom up fibonacci sequence dp
#def target nth number in the sequence
n = int(input("Please enter the desired term: "))

memo = [0 for n in range(0,n)]

def fibo(tgt):
  if tgt==0:
    return 0
  if tgt==1:
    return 1
  memo[0] = 1;
  memo[1] = 1;
  for n in range (2,tgt):
    memo[n]=memo[n-1]+memo[n-2]
  return memo[tgt-1]

print("The "+str(n)+" term in the fibonacci sequence is "+str(fibo(n)))