import random
import matplotlib.pyplot as plt

flips=int(input("How many flips?"))
heads=0
tails=0

for _ in range(flips):
    if random.choice(["Heads","Tails"])=="Heads":
        heads+=1
    else:
        tails+=1

print(f"Heads: ",heads)
print(f"Tails:",tails)

#experimental probability
exp_heads=heads/flips
exp_tails=tails/flips
print("-Experimental probability-")
print(f"Heads: {exp_heads:.2%}")
print(f"Tails: {exp_tails:.2%}")


#barchart
plt.figure(figsize=(6,4))
plt.bar(["Heads","Tails"],[heads,tails])
plt.title("Coin flip simulator")
plt.ylabel("Count")
plt.show()

#piechart
plt.figure(figsize=(7,6))
plt.pie([heads,tails],labels=["Heads","Tails"],autopct="%1.1f%%",startangle=90,colors=['lightblue','lightgreen'])
plt.title('Coin flip distribution')
plt.axis("equal")
plt.show()
