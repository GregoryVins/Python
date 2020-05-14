import timeit
import cProfile


def sieve(n):
    sieve = [i for i in range(n*20)]
    sieve[1] = 0
    for i in range(2, n*20):
        if sieve[i] != 0:
            j = i + i
            while j < n*20:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res[n - 1]

print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.1613099
print(timeit.timeit('sieve(200)', number=100, globals=globals()))  # 0.28515019999999996
print(timeit.timeit('sieve(400)', number=100, globals=globals()))  # 0.6571895
print(timeit.timeit('sieve(800)', number=100, globals=globals()))  # 1.2975065
print(timeit.timeit('sieve(1600)', number=100, globals=globals()))  # 3.3006354

cProfile.run('sieve(400)')  # 1    0.007    0.007    0.008    0.008 task_02.py:5(sieve)
cProfile.run('sieve(800)')  # 1    0.012    0.012    0.014    0.014 task_02.py:5(sieve)



def prime(n):
    prime = []
    for i in range(2, n * 10):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime[n - 1]

print(timeit.timeit('prime(50)', number=100, globals=globals()))  # 0.053415
print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 0.15811360000000002
print(timeit.timeit('prime(200)', number=100, globals=globals()))  # 0.5268566
print(timeit.timeit('prime(400)', number=100, globals=globals()))  # 1.7270081

cProfile.run('prime(100)')  # 1    0.002    0.002    0.002    0.002 task_02.py:29(prime)
cProfile.run('prime(200)')  # 1    0.005    0.005    0.006    0.006 task_02.py:29(prime)
