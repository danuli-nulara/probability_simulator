import random
import matplotlib.pyplot as plt

rolls=int(input("Nuumber of rolls:"))
results=[0]*6

for _ in range(rolls):
    roll=random.randint(1,6)
    results[roll-1]+=1

print("Results:")
for i in range(6):
    print(f"{i+1}: {results[i]}")

#barchart
plt.figure(figsize=(7,4))
plt.bar(range(1,7),results)
plt.title("Dice Roll frequency")
plt.ylabel("Count")
plt.show()

#piechart
plt.figure(figsize=(6,6))
plt.pie(results,labels=["1","2","3","4","5","6"],autopct="%1.1f%%",startangle=90,colors=['lightblue','lightgreen','orange','purple','red','grey'])
plt.title('Dice roll distribution')
plt.axis("equal")
plt.show()
