import factorial_cy
import time

# Test Cython implementation
start = time.time()
result = factorial_cy.factorial(900)
end = time.time()
print(f"Cython factorial time: {end - start:.6f} seconds")