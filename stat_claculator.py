import random
import statistics
import matplotlib.pyplot as plt

#generating some random numbers
count=int(input("How many random numbers?"))
minimum=int(input("Minimum value:"))
maximum=int(input("Maximum value:"))

numbers=[]

for _ in range(count):
    numbers.append(random.randint(minimum,maximum))
print(f"Generated numbers:",numbers)

print("Mean:",statistics.mean(numbers))
print("Median:",statistics.median(numbers))
print("Mode:",statistics.mode(numbers))
print("Minimum:",min(numbers))
print("Maximum:",max(numbers))

#histogram
plt.hist(numbers, bins=10,color='lightblue')
plt.title('Histogram of random numbers')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.show()