def check_prime(num):

    num = int(num)

    if num<=1:
        return False
    for divisors in range(2, num-1):
        if num%divisors == 0:
            return False
    return True

primes = []

x= int(input('How many prime numbers do you want:\n'))

for i in range(x):
    if check_prime(i):
        primes.append(i)
    print(primes)    
    

