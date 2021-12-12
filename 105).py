def fib_cycle(n):
    first = 1
    second = 1
    i = 0
    while i < n - 3:
      summ = first + second
      first = second
      second = summ
      i += 1
    print(second)
print(fib_cycle(10))
