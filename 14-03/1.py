
student_names = [
    'Caitlin',
    'Arthur',
    'Alena',
    'Ruth',
    'Olujoke'
]

print(student_names[0])

print('1st item', student_names[0])

student_names.append("Tania")
student_names.append("Tania")
print(student_names[0])

print('Arthur' in student_names)
print('James' in student_names)

print(student_names)
student_names.insert(0, 'Maryam')
print(student_names)


count = 0

for i in student_names:
    print(i)
# ????
print("Count", count)