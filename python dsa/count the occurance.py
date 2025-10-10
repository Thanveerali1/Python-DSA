my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = {}
for item in my_list:
    counts[item] = counts.get(item, 0) + 1
unique_list = list(dict.fromkeys(my_list))
print("Occurrences of each element:")
for item, count in counts.items():
    print(f"{item}: {count}")
print("\nList without duplicates:")
print(unique_list)
