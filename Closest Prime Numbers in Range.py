class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Edge case: If the given range is invalid
        if left > right:
            return [-1,-1]

        # Step1: Sieve of Eratosthenes
        is_prime = [True] * (right + 1) # Initialize all numbers as prime
        is_prime[0] = is_prime[1] = False # 0 and 1 are not prime numbers 


        # Mark non-prime numbers using the Sieve of Eratosthenes
        for i in range(2, int(right ** 0.5) + 1): # loop from 2 to sqrt(right)
            if is_prime[i]: # If 'i' is still marked as prime 
                for j in range(i * i, right + 1, i): # Mark all multiples of 'i' as non prime
                    is_prime[j] = False

        # Step 2: Collect primes in range
        primes = [i for i in range(left, right + 1) if is_prime[i]]

        # Step 3: If fewer than 2 primes exist, return [-1, -1]
        if len(primes) < 2: 
            return [-1, -1]

        # Step 4: Find the closest prime pair
        min_diff, num1, num2 = float('inf'), -1, -1

        # Iterate through the list of primes to find the smallest difference
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff: # Update if a smaller difference is found 
                min_diff = diff
                num1, num2 = primes[i - 1], primes[i]

        # Return the closest prime pair
        return [num1, num2]

        
