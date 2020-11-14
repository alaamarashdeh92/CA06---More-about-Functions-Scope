# Fibonacci Sequence


# TODO: Implement a recusrive fibonacci function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
 
n = 10
# Check if the number of terms is valid
if n <= 0:
   print("Plese enter a positive integer.")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fibonacci(i))