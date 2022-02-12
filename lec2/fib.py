def fib(n):
  """ Assumes n is an integer >= 0"""
  return 1 if (n == 0 or n == 1) else ( fib(n-1) + fib(n-2) )

def fastFib(n, memo = {0 : 1, 1 : 1}):
  """ Optimized form of fib using memoization, previous calculations are stored in a hash map"""
  if n in memo:
    return memo[n]
  else:
    result = fastFib(n-1, memo) + fastFib(n-2, memo)
    memo[n] = result
    return result