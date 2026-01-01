from collections import Counter

log_file = "logs/security.log"
attack_counter = Counter()

with open(log_file, "r") as file:
    for line in file:
        parts = line.strip().split(" | ")
        if len(parts) >= 4:
            attack_type = parts[2]
            attack_counter[attack_type] += 1

print("\nSentinelShield – Attack Summary Report\n")
print("{:<30}{}".format("Attack Type", "Count"))
print("-" * 45)

for attack, count in attack_counter.items():
    print("{:<30}{}".format(attack, count))
