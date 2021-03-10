# 1. 재귀적 호출
# 2. 동적계획법
____
# 3. 반복문
def fibonacci(n):
    if n==0 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

fibo = []
def fibonacci(n):
    if n==0 or n==1:
        return 1
    if fibo[n] != 0:
        return fibo[n]
    fibo[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibo[n]


def fibonacci(n):
    fibo[0] = 1
    fibo[1] = 1
    for i in n:
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]

# 방법 1. 일반 함수 사용 방식 (Function)
def fib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1

    for i in range(1,n):
        a,b = b, a+b

    return a

# 방법2. 재귀함수 사용 방식 (Recursive Function)
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


fib(5)

# 방법 3. 제네레이터 구현 방식 (Generator method)
def fibs():
    a,b = 0,1    // generator 출력할 때, next()로 다음것을 출력⇒ 한단계 늦춤
    while True:
        a,b = b, a+b
        yield a

f = fibs()
next(f)

# 방법 4. 메모이제이션 구현 방법 (Memoization Method)
def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList

fib(5)

# 방법 5. 파이썬 람다를 사용한 한줄 코딩 1 (Single Line Code with lambda)
fib = lambda n: 1 if n<=2 else fib(n-1) + fib(n-2)

fib(5)
