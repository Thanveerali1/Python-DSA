input_str = input("Enter a string: ")
frequency = {}

for char in input_str:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")