#Number to factorize (1.1)
num = 1537

#List to store the prime factors (1.2)
primeFactors = []

#Finding the prime factors using a loop (1.3)
factor = 2
while factor <= num:
    if num % factor == 0:
        primeFactors.append(factor)
        num //= factor
    else:
        factor += 1
        
#Printing the prime factors (1.4)
print(primeFactors)