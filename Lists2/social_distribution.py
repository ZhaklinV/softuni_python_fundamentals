population = list(map(int, input().split(", ")))
min_wealth = int(input())

sum_population = sum(population)

if (min_wealth * len(population)) > sum_population:
    print("No equal distribution possible")

else:
    for i in range(len(population)):
        wealthiest = max(population)
        index = population.index(wealthiest)
        if population[i] < min_wealth:
            diff = min_wealth - population[i]
            population[i] = min_wealth

            population[index] -= diff

    print(population)
