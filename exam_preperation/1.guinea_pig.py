total_food = float(input()) * 1000
total_hay = float(input()) * 1000
total_cover = float(input()) * 1000
guinea_weight = float(input()) * 1000

daily_food_gr = 300
out_of_stocks = False

for day in range(1, 31):
    total_food -= daily_food_gr
    if day % 2 == 0:
        total_hay -= (total_food * 0.05)
    if day % 3 == 0:
        total_cover -= (guinea_weight / 3)

    if total_food <= 0 or total_hay <= 0 or total_cover <= 0:
        out_of_stocks = True
        break

if out_of_stocks:
    print("Merry must go to the pet store!")

else:
    print(f"Everything is fine! Puppy is happy! Food: {(total_food/1000):.2f}, Hay: {(total_hay/1000):.2f}, Cover: {(total_cover/1000):.2f}.")
