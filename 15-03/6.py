import csv

with open("trees.csv", 'r') as file:
    spreadsheet = csv.DictReader(file)
    print(type(spreadsheet))

    heights = []

    for row in spreadsheet:
        tree_heights = row['height']
        heights.append(tree_heights)

    print(heights)
    shortest_height = min(heights)
    print(shortest_height)
