def calculate_min_budget(projects):
    projects.sort(key=lambda x: x[1] - x[2])  
    min_budget = 0
    current_budget = 0

    for project in projects:
        expenditure, bonus, penalty = project
        current_budget += expenditure
        min_budget = max(min_budget, current_budget + max(0, -penalty))

    return min_budget

n = int(input())
projects = []

for _ in range(n):
    expenditure, bonus_penalty, amount = input().split()
    expenditure = int(expenditure)
    bonus = int(bonus_penalty) if amount[0] == '+' else 0
    penalty = int(amount) if amount[0] == '-' else 0
    projects.append((expenditure, bonus, penalty))

result = calculate_min_budget(projects)
print(result)
