input_line = input()

final_sequence = ''
current_sequence = ''
for ch in range(len(input_line)):
    if ch + 1 < len(input_line) and input_line[ch].isdigit() and input_line[ch + 1].isdigit():
        current_sequence = current_sequence * int(input_line[ch:ch + 2])
        final_sequence += current_sequence
        current_sequence = ''
    elif input_line[ch].isdigit():
        n = int(input_line[ch])
        final_sequence += n * current_sequence
        current_sequence = ''
    else:
        current_sequence += input_line[ch]

final_sequence = final_sequence.upper()
unique_symbols = ''
for symb in final_sequence:
    if symb not in unique_symbols:
        unique_symbols += symb

print(f'Unique symbols used: {len(unique_symbols)}')
print(final_sequence)
