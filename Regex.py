# # Regex(Regular expressions) are patterns used to match character combinations in strings. 

# # Common Matching Patterns:
#     # re.match() - Determine if the RE matches at the beginning of the string.
#     # re.search() - Scan through a string, looking for any location where this RE matches
#     # re.findall() - Find all substrings where the RE matches, and returns them as a list.
#     # re.sub() - Replace all substrings where the RE matches with a specified string.
import re

Text = "The rain in Spain abhishek636@gmail.com +91 6383221055"
# re.Match():
    # re.match() checks for a match only at the beginning of the string.
print("re.match()")   
pattern = r"The"
result = re.match(pattern, Text)
print(result)  
# Output: <re.Match object; span=(0, 3), match='The'>


# re.search():
     # while re.search() checks for a match anywhere in the string.
print("re.search()")
pattern = r"ain"
result = re.search(pattern, Text)   
print(result)
# Output: <re.Match object; span=(5, 8), match='ain'>


# re.findall():
    # re.findall() finds all occurrences of the pattern in the string and returns them as a list.
print("re.findall()")
pattern = r'\b[A-Za-z]{3}\b'
result = re.findall(pattern, Text)
print(result)
# Output: ['ain', 'ain']


# Write a Regex pattern to match a valid email address from Text.
pattern = r'\w+@\w+\.\w+'
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
result = re.findall(pattern, Text)
print(result)
# Output: ['abhishek636@gmail.com']


# Write a Regex pattern to match a valid phone number from Text.
pattern = r'\+\b[0-9]{1,4}\b \b[0-9]{10,15}\b'
result = re.findall(pattern, Text)
print(result)
# Output: ['+91 6383221055']


# re.sub():
#     # re.sub() replaces all occurrences of the pattern in the string with a specified replacement
pattern = r'\w+@\w+\.\w+'
replacement = 'EMAIL_ADDRESS'
result = re.sub(pattern, replacement, Text)
print(result)
# Output: 'The rain in Spain EMAIL_ADDRESS PHONE_NUMBER'

pattern = r'\+\b[0-9]{1,4}\b \b[0-9]{10,15}\b'
replacement = 'PHONE_NUMBER'
result = re.sub(pattern, replacement, Text)
print(result)