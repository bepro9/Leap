# Fibonacci Series till limit
```python
def fibo(n):
    if(n == 0):
        print(0)
    if(n == 1):
        print(0, '\n', 1, '\n', 1, sep='')
    if(n > 1):
        a = 0
        b = 1
        print(a, end=' ')
        sum = a+b
        while(sum < n):
            print(sum, end=' ')
            sum = a+b
            a = b
            b = sum
    print()


limit = int(input("Enter you Limit of Fibonacci Series : "))
fibo(limit)

```
