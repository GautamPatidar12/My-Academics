'''
# 1. String Capitalization and Case Conversion Methods
a = "        Aashutosh Kumar Singh"

# Capitalize the first character of the string
print(a.capitalize())  # Output: '        aashutosh kumar singh'

# Convert the string to uppercase
print(a.upper())  # Output: '        AASHUTOSH KUMAR SINGH'

# Convert the string to lowercase
print(a.lower())  # Output: '        aashutosh kumar singh'

# Strip leading and trailing whitespace
print(a.strip())  # Output: 'Aashutosh Kumar Singh'


# 2. String Replacement and Substring Replacement
# Replace characters in the string
print(a.replace('a', 'B'))  # Output: '        BAshutosh KumBr Singh'

# Replace a specific substring with another substring
print(a.replace("Aashutosh", "Gudda"))  # Output: '        Gudda Kumar Singh'


# 3. String Splitting Methods
# Split string by spaces
print(a.split())  # Output: ['Aashutosh', 'Kumar', 'Singh']

# Split string by a specific character (space in this case)
print(a.split(" "))  # Output: ['', '', '', 'Aashutosh', 'Kumar', 'Singh']

# Split string by the letter 'a'
print(a.split("a"))  # Output: ['        ', 'shutosh Kum', 'r Singh']


# 4. String Concatenation
first = "Gautam "
last = "Patidar"
print(first + last)  # Output: 'Gautam Patidar'


# 5. Arithmetic with Strings (When Convertible to Numbers)
a = 5.5
b = 7
print(a + b)  # Output: 12.5

a = "5.5"
b = "7"
print(a + b)  # Output: '5.57'


# 6. Title Case, Left Strip, Right Strip Methods
a = "   aashutosh kumar singh   "

# Convert string to title case
print(a.title())  # Output: '   Aashutosh Kumar Singh   '

# Remove leading spaces
print(a.lstrip())  # Output: 'aashutosh kumar singh   '

# Remove trailing spaces
print(a.rstrip())  # Output: '   aashutosh kumar singh'


# 7. Join Method for List to String
a = ["Aashutosh ", "Kumar"]
print("".join(a))  # Output: 'Aashutosh Kumar'


# 8. String Search Methods (find)
a = "Aashutosh Kumar"

# Search for a character in the string and return its index (returns -1 if not found)
print(a.find("z"))  # Output: -1
print(a.find("o"))  # Output: 3
print(a.find("a"))  # Output: 0
print(a.find("K"))  # Output: 11


# 9. Alpha and Digit Check
a = "123Aashutosh Kumar"

# Check if string contains only alphabetic characters
print(a.isalpha())  # Output: False

# Check if string contains only numeric digits
print(a.isdigit())  # Output: False


# 10. String Formatting with format() Method
a = "Gautam Patidar{}"
b = 1209
print(a.format(b))  # Output: 'Gautam Patidar1209'

a = "{}Gautam Patidar"
b = 1209
a = a.format(b)  # Output: '1209Gautam Patidar'


# 11. Character and Unicode Methods (ord and chr)
# Print Unicode values for characters
a = "123Aashutosh Kumar"
print(ord("a"))  # Output: 97
print(ord("A"))  # Output: 65
print(ord("@"))  # Output: 64
print(ord("."))  # Output: 46

# Print Unicode values for all lowercase characters
p = "abcdefghijklmnopqrstuwxyz"
for i in p:
    print(ord(i), end=" ")  # Outputs Unicode values for all lowercase letters

# Print Unicode values for all uppercase characters
for i in p:
    x = i.upper()
    print(ord(x), end=" ")  # Outputs Unicode values for all uppercase letters

# Example of converting a Unicode value back to character using chr()
print(chr(69))  # Output: 'E'


# 12. Type Conversion (Integer to String)
a = 2004
print(type(a), "\n", str(a), "\n", type(str(a)))  # Output: <class 'int'>, '2004', <class 'str'>'''