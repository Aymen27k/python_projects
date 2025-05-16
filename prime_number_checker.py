def prime_checker(number):
    if number <= 1:
        print(f"{n} is not a prime number")
        return
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a Prime number!")


n = int(input("Check this number : "))
prime_checker(n)
