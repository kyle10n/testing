def fibonacci(n):
  if n is 1 or 2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)
