# 1. Count Even and Odd Numbers in a List
Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = 0
odd_count = 0
for num in Numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")


# 2. Find Second Largest Number in a List
List = [10, 20, 4, 45, 99]
List.sort()
print(List[-2])



# 3. Remove Duplicates Using Set
Numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7]
Numbers = list(set(Numbers))
print(Numbers)


# 4. Find Common Elements Between Two Lists
List1 = [1, 2, 3, 4, 5]
List2 = [4, 5, 6, 3, 8]
common_elements = list(set(List1) & set(List2))
print(common_elements)


# 5. Frequency Count of Elements
numbers = [1, 2, 3, 4, 3, 2, 3, 3, 3]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)
        


# 6. Reverse a List Without Slicing
list1 = [1, 2, 3, 4, 5]
reversed_list = []
for i in list1:
    reversed_list.insert(0, i)
print(reversed_list)

# 7. Find Missing Numbers from Range
Numbers = [1, 2, 4, 6, 7, 9]
missing_numbers = []
for i in range(1, 10):
    if i not in Numbers:
        missing_numbers.append(i)
print(missing_numbers)

# 8. Check Palindrome String
string = input("Enter a string: ")
cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 9. Count Vowels and Consonants
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

# 10. Find Largest Word in a Sentence.
text = "The quick brown fox jumps over the lazy dog"
words = text.split()
largest_word = max(words, key=len)
print(len(largest_word))
print(largest_word)


# 11. Merge Two Dictionaries
dic1 = {"Obito": 100000, "Sukuna": 75000}
dic2 = {"Naruto": 50000, "Kakashi": 60000}
dic1.update(dic2)
print(dic1)

# 12. Sort Dictionary by Values
dic = {"Obito": 100000, "Sasuke": 75000, "Naruto": 50000, "Kakashi": 60000}
result = []
result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
print(result)


# 13. Find Duplicate Elements in List
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7]
duplicates = []
for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)


# 14. Create Dictionary from Two Lists
keys = ['Toji', 'Sukuna', 'Gojo', 'Itadori']
values = [100000, 75000, 50000, 60000]
list_dict = []
for i in range(len(keys)):
    list_dict.append({keys[i]: values[i]})
print(list_dict)


# 15. Find Union of Two Sets
S1 = {1, 2, 3, 4, 8}
S2 = {4, 5, 6, 7, 8}
print(S1.union(S2))


# 16. Find Intersection of Two Sets
s1 = {1, 2, 3, 4, 8}
s2 = {4, 5, 6, 7, 8}
print(s1.intersection(s2))


# 17. Find Difference Between Sets
Set1 = {1, 2, 3, 4, 5}
Set2 = {4, 5, 6, 7, 8}
print(Set1.difference(Set2))


# 18. Count Positive, Negative and Zero
numbers = [1, -2, 3, 0, -5, 6, 0, 4]
pov = neg = zero = 0
for num in numbers:
    if num > 0:
        pov += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print(f"Positive numbers: {pov}, Negative numbers: {neg}, Zeroes: {zero}")


# 19. Nested Dictionary Traversal
Employees = {
    "E01": {"Name": "Toji", "Salary": 100000},
    "E02": {"Name": "Sukuna", "Salary": 75000},
    "E03": {"Name": "Gojo", "Salary": 50000},
    "E04": {"Name": "Itadori", "Salary": 60000}
}
for emp_id, emp_info in Employees.items():
    print(emp_id,emp_info["Name"],emp_info["Salary"])


# 20. Find Employee with Highest Salary
Employee = {"Toji": 100000, "Sukuna": 75000, "Gojo": 50000, "Itadori": 60000}
highest_salary = max(Employee.values())

for name, salary in Employee.items():
    if salary == highest_salary:
        print(f"{name} has the highest salary of {salary}")


# 21. Membership Operator Validation
name = ["Toji", "Sukuna", "Gojo", "Itadori"]
user_name = input("Enter your name: ")
if user_name in name:
    print(f"Welcome {user_name}")
else:
    print("You are not a member. Please register first.")


# 22. Login Attempt Using While Loop
password = "@Admin000"
attempts = []
while attempts != password:
    attempts = input("Enter your password: ")
    if attempts == password:
        print("Login Successful")
    else:
        print("Incorrect Password. Try Again.")
        break

# 23. Categorize Marks Using Nested If
Mark = int(input("Enter your marks: "))
if Mark >= 35:
    if Mark >= 90:
        print("You got Distinction")
    elif Mark >= 75:
        print("You got First Class")
    elif Mark >= 60:
        print("You got Second Class")
    else:
     print("You pass the Exam")
else:
    print("You failed in the Exam")



# 24. Find Unique Elements from Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
for i in list1 + list2:
    if i not in list1 or i not in list2:
        print(i)


# 25. Student Result Analysis Using Dictionary
Dic = {"Sukuna" : 99, "Gojo" : 75, "Itadori" : 60, "Megumi" : 80}

for name,mark in Dic.items():
    if mark >= 90:
        print(f"{name} has scored A grade with marks {mark}")
    elif mark >= 80:
        print(f"{name} has scored B grade with marks {mark}")
    elif mark >= 70:
        print(f"{name} has scored C grade with marks {mark}")
    elif mark >= 60:
        print(f"{name} has scored D grade with marks {mark}")
    else:
        print(f"{name} has failed with marks {mark}")