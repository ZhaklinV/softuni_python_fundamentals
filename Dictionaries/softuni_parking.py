def final_print(users_dic):
    for user_name, car_num in users_dic.items():
        print(f"{user_name} => {car_num}")


def parking_validation(status, name, license_plate_number, parking_users):
    if status == "register":
        if name not in parking_users:
            parking_users[name] = license_plate_number
            print(f"{name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_users[name]}")

    elif status == "unregister":
        if name not in parking_users:
            print(f"ERROR: user {name} not found")
        else:
            del parking_users[name]
            print(f"{name} unregistered successfully")


def input_processing(integer):
    car_number = ''
    parking_users = {}
    for i in range(integer):
        input_data = input().split()
        info = input_data[0]
        username = input_data[1]
        if info == "register":
            car_number = input_data[2]

        parking_validation(info, username, car_number, parking_users)
    final_print(parking_users)


n = int(input())
input_processing(n)
