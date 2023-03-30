def cast_spell(name, mp_needed, spell_name):
    current_mp = heroes_info[name]['MP']
    if current_mp >= mp_needed:
        heroes_info[name]['MP'] -= mp_needed
        print(f"{name} has successfully cast {spell_name} and now has {heroes_info[name]['MP']} MP!")

    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")


def take_damage(name, damage, attacker):
    current_hp = heroes_info[name]['HP']
    reducing = current_hp - damage
    if reducing <= 0:
        heroes_info.pop(name)
        print(f"{name} has been killed by {attacker}!")
    else:
        heroes_info[name]['HP'] -= damage
        print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes_info[name]["HP"]} HP left!')


def recharge(name, amount):
    current_mp = heroes_info[name]['MP']
    if current_mp + amount > 200:
        amount = 200 - current_mp
        heroes_info[name]['MP'] = 200

    else:
        heroes_info[name]['MP'] += amount

    print(f"{name} recharged for {amount} MP!")


def heal(name, amount):
    current_hp = heroes_info[name]['HP']
    if current_hp + amount > 100:
        amount = 100 - current_hp
        heroes_info[name]['HP'] = 100

    else:
        heroes_info[name]['HP'] += amount

    print(f"{name} healed for {amount} HP!")


n = int(input())
heroes_info = {}

for _ in range(n):
    hero_name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200
    heroes_info[hero_name] = {'HP': hp, 'MP': mp}

command = input()

while not command == "End":
    action, hero_name, *info = [int(item) if item.isdigit() else item for item in command.split(" - ")]

    if action == 'CastSpell':
        cast_spell(hero_name, *info)

    elif action == 'TakeDamage':
        take_damage(hero_name, *info)

    elif action == 'Recharge':
        recharge(hero_name, *info)

    elif action == 'Heal':
        heal(hero_name, *info)

    command = input()

for item in heroes_info:
    print(item)
    print(f'  HP: {heroes_info[item]["HP"]}')
    print(f'  MP: {heroes_info[item]["MP"]}')