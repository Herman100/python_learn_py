def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


n = int(input("Enter the number of terms in the Fibonacci sequence: "))

print(f"The first {n} terms of the Fibonacci sequence are: {fibonacci_sequence(n)}")


# draw the fibonacci sequence import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

n = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci_sequence = fibonacci_sequence(n)

plt.plot(fibonacci_sequence)
plt.title("Fibonacci Sequence")
plt.xlabel("Term")
plt.ylabel("Value")
plt.show()
