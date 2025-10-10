item1 = 'apple'
item2 = 'banana'
item3 = 'apple'
item4 = 'orange'
item5 = 'banana'
item6 = 'apple'

apple_count = 0
banana_count = 0
orange_count = 0

if item1 == 'apple':
    apple_count += 1
elif item1 == 'banana':
    banana_count += 1
elif item1 == 'orange':
    orange_count += 1

if item2 == 'apple':
    apple_count += 1
elif item2 == 'banana':
    banana_count += 1
elif item2 == 'orange':
    orange_count += 1

if item3 == 'apple':
    apple_count += 1
elif item3 == 'banana':
    banana_count += 1
elif item3 == 'orange':
    orange_count += 1

if item4 == 'apple':
    apple_count += 1
elif item4 == 'banana':
    banana_count += 1
elif item4 == 'orange':
    orange_count += 1

if item5 == 'apple':
    apple_count += 1
elif item5 == 'banana':
    banana_count += 1
elif item5 == 'orange':
    orange_count += 1

if item6 == 'apple':
    apple_count += 1
elif item6 == 'banana':
    banana_count += 1
elif item6 == 'orange':
    orange_count += 1

print("Occurrences of each element:")
print("apple:", apple_count)
print("banana:", banana_count)
print("orange:", orange_count)

print("\nList without duplicates:")
print("apple")
print("banana")
print("orange")
