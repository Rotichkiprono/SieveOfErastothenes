def sieve_of_eratosthenes(n):
  """
  This function finds all prime numbers up to a given number (n) using the Sieve of Eratosthenes algorithm.

  Args:
      n: The upper limit for finding prime numbers.

  Returns:
      A list containing all prime numbers less than or equal to n.
  """
  # Create a boolean list to mark if a number is prime (True) or composite (False)
  is_prime = [True] * (n + 1) 
  is_prime[0] = is_prime[1] = False  # Exclude 0 and 1

  # Iterate through potential primes (up to the square root of n)
  for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
      # Mark all multiples of i as composite
      for j in range(i * i, n + 1, i):
        is_prime[j] = False

  # Return the list of primes based on the is_prime list
  return [i for i, is_prime_val in enumerate(is_prime) if is_prime_val]

# Example usage
n = 100
primes = sieve_of_eratosthenes(n)
print(f"Prime numbers less than or equal to {n}: {primes}")
