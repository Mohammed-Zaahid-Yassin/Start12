def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

while True:
    print("\nPrime Number Utility Menu:")
    print("1. Check if a number is prime")
    print("2. Generate all primes up to a number")
    print("3. Quit")

    choice = input("Choose an option (1/2/3): ")
    if choice == "1":
        num = int(input("Enter the number to check: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    elif choice == "2":
        limit = int(input("Generate primes up to (inclusive): "))
        primes = generate_primes(limit)
        print(f"Prime numbers up to {limit}:")
        print(primes)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
