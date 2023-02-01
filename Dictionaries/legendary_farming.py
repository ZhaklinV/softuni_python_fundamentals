input_data = input().split()
legendary_item = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
is_win = False

while True:
    # for i in range(0, len(input_data), 2):
    #     quantity, material = int(input_data[i]), input_data[i + 1].lower()
    for quantity, material in zip(input_data[0::2],input_data[1::2]):
        material = material.lower()
        quantity = int(quantity)

        if material == "shards" or material == "fragments" or material == "motes":
            if material not in legendary_item:
                legendary_item[material] = 0
            legendary_item[material] += int(quantity)
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += int(quantity)

        for key, value in legendary_item.items():
            if value >= 250:
                legendary_item[key] = value - 250
                is_win = True

                special_item = " "
                if key == "shards":
                    special_item = "Shadowmourne"
                elif key == "fragments":
                    special_item = "Valanyr"
                elif key == "motes":
                    special_item = "Dragonwrath"

                print(f"{special_item} obtained!")

        if is_win:
            break
    if is_win:
        break
    input_data = input().split()

print(f"shards: {legendary_item['shards']}")
print(f"fragments: {legendary_item['fragments']}")
print(f"motes: {legendary_item['motes']}")

for x, y in junk.items():
    print(f"{x}: {y}")
