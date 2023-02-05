# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros,
# and moves them to the back without messing up the other elements. Print the resulting integer list
# input: 0, 5, 0, 4, 0, 0, 5

input_line = input().split(", ")
int_list = list(map(int,input_line))

for i in range(len(int_list)):
    if int_list[i] == 0:
        int_list.remove(0)
        int_list.append(0)

print(int_list)
