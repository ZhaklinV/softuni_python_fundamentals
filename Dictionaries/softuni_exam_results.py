def printing(user_info, submission_dict):
    print("Results:")
    for el in user_info:
        for name, points_ in user_info[el].items():
            print(f"{name} | {points_}")

    print("Submissions:")
    if is_banned:
        for course in user_info.keys():
            print(f"{course} - {submission_dict[course]}")
    else:
        for k, value in submission_dict.items():
            submission = value
            print(f"{k} - {submission}")


def ban_users(username_, info_dict):
    for key in info_dict:
        if username_ in info_dict[key]:
            del info_dict[key][username_]

    return info_dict


def create_info(username_, language, points, user_info_dict):
    if language not in user_info_dict:
        user_info_dict[language] = {}
    if username_ not in user_info_dict[language]:
        user_info_dict[language][username_] = int(points)
    else:
        if int(user_info_dict[language][username_]) < int(points):
            user_info_dict[language][username_] = int(points)

    return user_info_dict


input_line = input()
user_info_dict = {}
submission_dic = {}
is_banned = False

while input_line != "exam finished":

    if "banned" not in input_line:
        username, language, points = input_line.split("-")

        if language not in submission_dic:
            submission_dic[language] = 0
        submission_dic[language] += 1
        create_info(username, language, points, user_info_dict)

    else:
        input_line = input_line.split("-")
        username = input_line[0]
        is_banned = True

        ban_users(username, user_info_dict)

    input_line = input()

printing(user_info_dict, submission_dic)
print()
