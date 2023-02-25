# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

import string

usernames = input().split(", ")

for name in usernames:
    if 3 <= len(name) <= 16:
        for letter in name:
            if letter not in "-_" + string.ascii_letters + string.digits:
                break
        else:
            print(name)

