def drive(name, distance, needed_fuel):
    current_fuel = car_info[name]['fuel']
    if current_fuel < needed_fuel:
        print("Not enough fuel to make that ride")
    else:
        car_info[name]['mileage'] += distance
        car_info[name]['fuel'] -= needed_fuel
        print(f"{name} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")


def refuel(name, refill):
    current_fuel = car_info[name]['fuel']
    if current_fuel + refill > 75:
        car_info[name]['fuel'] = 75
        refill = 75 - current_fuel
    else:
        car_info[name]['fuel'] += refill

    print(f"{name} refueled with {refill} liters")


def revert(name, km):
    moment_mileage = car_info[car_type]['mileage']
    if moment_mileage - km < 10000:
        car_info[car_type]['mileage'] = 10000
    else:
        car_info[car_type]['mileage'] -= km
        print(f"{name} mileage decreased by {km} kilometers")


count_car = int(input())
car_info = {}

for _ in range(count_car):
    car, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
    car_info[car] = car_info.get(car, {'mileage': mileage, 'fuel': fuel})

command = input()

while not command == 'Stop':
    action, car_type, *info = [int(item) if item.isdigit() else item for item in command.split(" : ")]

    if action == 'Drive':
        drive(car_type, *info)

    elif action == 'Refuel':
        refuel(car_type, *info)

    elif action == 'Revert':
        revert(car_type, *info)

    current_mileage = car_info[car_type]['mileage']
    if current_mileage >= 100000:
        car_info.pop(car_type)
        print(f"Time to sell the {car_type}!")

    command = input()

for element in car_info:
    print(f"{element} -> Mileage: {car_info[element]['mileage']} kms, Fuel in the tank: {car_info[element]['fuel']} lt.")
