n = int(input())
synonyms_dictionary = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonyms_dictionary:
        synonyms_dictionary[word] = []

    synonyms_dictionary[word].append(synonym)

for w, s in synonyms_dictionary.items():
    print(f'{w} - {", ".join(s)}')
