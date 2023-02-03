def printing(force_dict):
    for key, value in force_dict.items():
        if len(value) > 0:
            print(f"Side: {key}, Members: {len(value)}")
            for el in value:
                print(f"! {el}")


def create_force_side(side, user, user_info_dict):
    already_exist = False
    if side not in user_info_dict:
        user_info_dict[side] = []
    for el in user_info_dict.values():
        if user in el:
            already_exist = True
    if already_exist is not True:
        user_info_dict[side].append(user)

    return user_info_dict


def create_user(force_user_, force_side_, sides_dic_):
    for current_side in sides_dic_:
        if force_user_ in sides_dic_[current_side]:
            for i in range(len(sides_dic_[current_side])):
                sides_dic_[current_side].pop(i)
                break

    if force_side_ in sides_dic_:
        sides_dic_[force_side_].append(force_user_)
    else:
        sides_dic_[force_side_] = force_user_
    print(f"{force_user_} joins the {force_side_} side!")


input_data = input()
sides_dic = {}

while True:

    if input_data == "Lumpawaroo":
        break

    if "|" in input_data:
        input_data = input_data.split(" | ")
        force_side, force_user = input_data[0], input_data[1]

        create_force_side(force_side, force_user, sides_dic)

    elif "->" in input_data:
        input_data = input_data.split(" -> ")
        force_user, force_side = input_data[0], input_data[1]

        create_user(force_user, force_side, sides_dic)

    input_data = input()

printing(sides_dic)