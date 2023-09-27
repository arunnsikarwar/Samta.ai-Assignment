def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

def main():
    try:
        n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
        
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence = generate_fibonacci(n)
            print("Fibonacci sequence:")
            for number in fibonacci_sequence:
                print(number, end=" ")
    except ValueError:
        print("Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
