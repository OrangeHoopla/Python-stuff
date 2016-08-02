def isPrime(n):
    if n == 2: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True
if __name__ == "__main__":
    n = 1
    count = 2
    while n < 2000001:
        n += 2
        if isPrime(n): count += n
    print count