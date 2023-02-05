# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.

n = int(input())
courses = []

for i in range(n):
    item = input()
    courses.append(item)

print(courses)