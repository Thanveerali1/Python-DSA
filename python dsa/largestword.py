input_str = input("Enter a string: ")
words = input_str.split()

if words:
    largest_word = max(words, key=len)
    print("The largest word is:", largest_word)
else:
    print("No words found in the string.")