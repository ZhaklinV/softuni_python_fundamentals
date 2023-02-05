# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

number = int(input())
positive = []
negative = []

for i in range(number):
    input_num = int(input())
    if input_num >= 0:
        positive.append(input_num)
    else:
        negative.append(input_num)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}\nSum of negatives: {sum(negative)}")
