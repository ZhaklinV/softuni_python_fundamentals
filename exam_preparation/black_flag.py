days_of_plunder = int(input())
daily_plunder = int(input())
target = float(input())
current_plunder = 0

for day in range(1,days_of_plunder+1):
    current_plunder += daily_plunder
    if day % 3 == 0:
        current_plunder += (daily_plunder / 2)
    if day % 5 == 0:
        current_plunder *= 0.7

if current_plunder >= target:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    left = (current_plunder/target)*100
    print(f"Collected only {left:.2f}% of the plunder.")
