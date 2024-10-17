def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)
print("Enter a value:")
n=int(input())
print("The Factorial of ",n,"is :" ,fact(n))
