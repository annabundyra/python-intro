"""
CFG Graduation Photo Challenge -- SOLUTION

"""

purple_hats_heights = [5, 5, 1, 3, 4]
black_hats_heights = [6, 9, 2, 4, 5]

def is_possible_photo(software_students, data_students):
    software_students.sort()
    data_students.sort()
    output = True
    if len(software_students) == len(data_students):

        if (software_students[0] > data_students[0]):
            first_row = "BLACK"
        else:
            first_row = "PURPLE"

        for i in range(len(software_students)):

            if(first_row == "BLACK"):
                if (software_students[i] <= data_students[i]):
                    output = False

            else:
                if (data_students[i] <= software_students[i]):
                    output = False
    return output

print(is_possible_photo(purple_hats_heights, black_hats_heights))

# def is_possible_photo(purple, black):
#     """
#     Calculate whether we can take guidelines compliant photo.
#     :param purple: list of ints - students in purple hats heights
#     :param black: list of ints - students in black hats heights
#     :return: boolean
#     """
#     purple.sort()
#     black.sort()
#
#     first_row_colour = "PURPLE" if purple[0] < black[0] else "BLACK"
#
#     for idx in range(len(purple)):
#         purple_height = purple[idx]
#         black_height = black[idx]
#
#         if first_row_colour == 'PURPLE':
#             if purple_height >= black_height:
#                 return False
#         else:
#             if black_height >= purple_height:
#                 return False
#     return True
#



# [90, 40, 30]
# [70, 8, 100]
# # Sort the lists
# # Determine front and back list
# front_list = [ 8,  70, 100]
# back_list =  [ 30,40, 90]
# # Compare the people at the same positions
