
primes = []
upto = 10000000

for candidate in range (2,upto):
    #print (candidate)
    isPrime = True
    #for divisor in range (2,candidate):
    for divisor in primes:
        if (candidate % divisor == 0):
            isPrime = False
            break
    if isPrime:
        primes.append(candidate)

print(primes)