numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for number in numbers:
    if number <= 1:
        continue
    if number == 2:
        primes.append(number)
        continue
    if number % 2 == 0:
        not_primes.append(number)
        continue
    for idx in range (3, int(number**0.5)+1, 2):
        if number % idx == 0:
            is_prime = False
        else:
            is_prime = True
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)


print(primes)
print(not_primes)



# numbers primes not_primes range
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
