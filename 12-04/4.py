
students = [
    {'name': 'Jane', 'age': 43, 'specialization': 'Software'},
    {'name': 'Priya', 'age': 24, 'specialization': 'Data'},
    {'name': 'Diana', 'age': 18, 'specialization': 'Data'}

]

# get info for a student called 'Priya' ( a search criteria can be anything:
# an ID, a name, name and surname together and many more)

result = list(filter(lambda student : student['name'] == 'Priya', students))  # todo:  use filter to return a list containing student with name 'Priya'
print(result)