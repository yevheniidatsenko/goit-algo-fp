import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_simulations=10000):
  sum_counts = {i: 0 for i in range(2, 13)} 

  for _ in range(num_simulations):  
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6)  
    result_sum = die1 + die2 
    sum_counts[result_sum] += 1 

  probabilities = {s: count / num_simulations for s, count in sum_counts.items()}  
  probabilities_percent = {s: p * 100 for s, p in probabilities.items()} 

  return probabilities_percent


def plot_probabilities(probabilities_percent):
  sums = list(probabilities_percent.keys())
  probs = list(probabilities_percent.values())

  plt.figure(figsize=(10, 6))
  plt.bar(sums, probs, color="skyblue")  
  plt.xlabel("Sum")  
  plt.ylabel("Probability (%)")  
  plt.title("Probabilities of each sum when rolling two dice") 
  plt.xticks(sums) 
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.show()


def main():
  probabilities_percent = simulate_dice_rolls()

  print("Probabilities of each sum (in percentages):")
  for s, p in probabilities_percent.items():
    print(f"Sum {s}: {p:.2f}%")

  plot_probabilities(probabilities_percent)


if __name__ == "__main__":
  main()