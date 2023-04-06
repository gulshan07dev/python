# list are changeable
# list index -> 0 (zero based index)

marks = [3, 5, 6, 2, 8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# negative index
print(marks[-2])  # len(marks)-2 -> 1 => 5

# check- 7 is present or not int list
if 7 in marks:
    print("Yes")
else:
    print("No")


if "Gulsh" in "Gulshan":
    print("Yes")
else:
    print("No")

# Same thing applied for string as well!

print(marks[0:5]) # or print(marks[:]) or print(marks)