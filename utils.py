def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number (sum of proper divisors equals the number)."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def digit_sum(n: int) -> int:
    """Calculate the sum of a number's digits."""
    return sum(int(d) for d in str(abs(n)))

def get_number_properties(n: int):
    """Determine the number's properties (Armstrong, even, odd)."""
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("even" if n % 2 == 0 else "odd")
    return properties
