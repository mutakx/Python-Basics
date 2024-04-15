example = "hello"

print(example[::-1])





example2 = "racecar"
reverse_example2 = example2[::-1]

is_palindrome=example2==reverse_example2
print(is_palindrome)




example3 = "hello"
vowels = "aeiou"
count_vowels=len([char for char in example3 if char in vowels])
print(count_vowels)
