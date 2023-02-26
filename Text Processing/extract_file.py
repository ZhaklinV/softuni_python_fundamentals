# Write a program that reads the path to a file and subtracts the file name and its extension.

path = input().split("\\")

file = path[-1]
file_name, file_extension = file.split('.')

print(f'File name: {file_name}')
print(f'File extension: {file_extension}')
