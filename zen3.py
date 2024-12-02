# Function to generate Fibonacci series using lambda
def fibonacci_series(n):
    fib = [1, 2]  # Starting values for Fibonacci series

# Generate Fibonacci series using a loop and lambda
    list(map(lambda _: fib.append(fib[-1] + fib[-2]), range(2, n)))  # Generate up to n terms
    return fib[:n]  # Return only the first n terms

# Main code
n = 50
fib_numbers = fibonacci_series(n)
print(f"The first {n} Fibonacci numbers are: {fib_numbers}")
