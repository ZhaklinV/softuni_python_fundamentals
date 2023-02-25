input_line = input().split()
final_str = ''

for word in input_line:
    final_str += len(word) * word  # конкатениране

print(final_str)