items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    """
    Greedy algorithm to select items with maximum calories-to-cost ratio
    """
    items_sorted = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    for item, props in items_sorted:
        if total_cost + props["cost"] <= budget:
            selected_items.append(item)
            total_cost += props["cost"]
            total_calories += props["calories"]
    return selected_items, total_calories

def dynamic_programming(budget):
    """
    Dynamic programming to find the optimal set of items for maximum calories
    """
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    items_list = list(items.keys())
    for i in range(1, len(items) + 1):
        item = items_list[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        for j in range(1, budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
    selected_items = []
    j = budget
    for i in range(len(items), 0, -1):
        item = items_list[i - 1]
        cost = items[item]["cost"]
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(item)
            j -= cost
    return selected_items, dp[-1][-1]

# Test the functions
budget = 100
print("Greedy Algorithm:")
selected_items, total_calories = greedy_algorithm(budget)
print("Selected items:", selected_items)
print("Total calories:", total_calories)

print("\nDynamic Programming:")
selected_items, total_calories = dynamic_programming(budget)
print("Selected items:", selected_items)
print("Total calories:", total_calories)