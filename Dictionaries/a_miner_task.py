# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"

input_data = input()
collected_resources = {}

while input_data != "stop":
    resource = input_data
    quantity = int(input())

    if resource not in collected_resources:
        collected_resources[resource] = 0
    collected_resources[resource] += quantity

    input_data=input()

for products, count in collected_resources.items():
    print(f'{products} -> {count}')
