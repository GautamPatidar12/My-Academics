'''
# String Indexing and Slicing Examples

a = "Learning Python"

# Access specific characters using positive indexing
print(a[6])  # Output: 'n' (Character at index 6)
print(a[9])  # Output: 'h' (Character at index 9)
print(a[3])  # Output: 'r' (Character at index 3)
print(a[-5])  # Output: 't' (Character at index -5)

# Slice the string from the beginning to index 9 (not including index 9)
print(a[0:9])  # Output: 'Learning' (First 9 characters)

# Slice the string from index 9 to the end
print(a[9:])  # Output: ' Python' (Characters from index 9 to the end)

# Iterate over each character in the string and print with spaces in between
for i in a:
    print(i, end=" ")  # Output: L e a r n i n g   P y t h o n 

print("\n")

# Iterate over each index of the string and print the character at each index
for i in range(len(a)):
    print(a[i], end=" ")  # Output: L e a r n i n g   P y t h o n 

print("\n")

# Iterate over the string with a step of 3 (print every third character)
for i in range(0, len(a), 3):
    print(a[i], end=" ")  # Output: L r n P t h 

# Print the string in reverse order using negative indexing
for i in range(-1, -len(a)-1, -1):
    print(a[i], end=" ")  # Output: n o h t y P   g n i r a e L

# Reverse the string using slicing
print(a[-1::-1])  # Output: nohtyP gninraeL

# Print the entire string (this is just the original string)
print(a[::])  # Output: 'Learning Python'

# Print the entire string with a step of 1 (this is the same as the original string)
print(a[::1])  # Output: 'Learning Python'

# Print every second character of the string
print(a[::2])  # Output: 'Lann yhn'

# Slice the string from index 2 to 9 and step by 2
print(a[2:9:2])  # Output: 'aig'


# Palindrome Checking Logic
a = eval(input("Give the string: "))  # Takes input from user

# Create a variable b that is the same as the original string
b = a[::]

# Create a variable c that is the reverse of the original string
c = a[-1::-1]

# Check if the string is the same forwards and backwards
if b == c:
    print("It is a palindrome")  # If the string is the same, it's a palindrome
else:
    print("It is not a palindrome")  # If the string is different, it's not a palindrome
'''