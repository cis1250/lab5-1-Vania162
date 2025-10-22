#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_user_input():
  while True:
    try:
      terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
      if terms <= 0:
        print("Error: Please enter a positive integer.")
      else:
        return terms
    except ValueError:
      print("Error: Invalid input. Please enter a valid integer.")

def generate_Fibonacci_sequence(n):
  sequence = []
  a, b = 0, 1
  
  for i in range (n):
    sequence.append(a)
    a, b = b, a + b
  
  return sequence

def print_sequence(sequence):
  print("\nFibonacci Sequence:")
  print(", ".join(map(str, sequence)))


def main():
  num_terms = get_user_input()
  fib_sequence = generate_fibonacci(num_terms)
  print_sequence(fib_sequence)

main()
