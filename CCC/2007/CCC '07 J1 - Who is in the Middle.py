weights = []

for i in range(3):
    weight_value = int(input())
    weights.append(weight_value)
    
sorted_weights = sorted(weights)

print(sorted_weights[1])
