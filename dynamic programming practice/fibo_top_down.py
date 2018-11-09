#quick and dirty top down fibonacci sequence dp
#def target nth number in the sequence
n = int(input("Please enter the desired term: "))

memo=[-1 for x in range(0,n)]
#0 index adjustment
call=n-1
def fibo(tgt):
  if tgt < 2:
    memo[tgt] = 1;
    return 1;
  if memo[tgt]==-1:
    memo[tgt]=fibo(tgt-1)+fibo(tgt-2)
  return memo[tgt]
  
print("The "+str(n)+" term in the fibonacci sequence is "+str(fibo(call)))