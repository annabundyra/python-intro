def calculate_classes(num_students):
    """
    This function calculates the minimum number of classes needed to accommodate a given number of students.

    Parameters:
        num_students (int): The number of students to accommodate in the classes.

    Returns:
        A tuple containing:
        - A string that shows the proposed number of classes.
        - A dictionary that shows the allocation of students in each class.
    """
    # Define the maximum number of students per class
    max_students_per_class = 30

    # Calculate the number of classes needed
    num_classes = max(2, (num_students + max_students_per_class - 1) // max_students_per_class)

    # Allocate the students to the classes
    class_size = (num_students + num_classes - 1) // num_classes
    class_allocation = {}
    for i in range(num_classes):
        start = i * class_size + 1
        end = min(start + class_size, num_students + 1)
        class_allocation[f"Class {i+1}"] = list(range(start, end))

    # Format the output string
    if num_classes == 1:
        classes_str = "1 class"
    else:
        classes_str = f"{num_classes} classes"

    # Return the result as a tuple
    result_str = f"We need {classes_str} to accommodate {num_students} students."
    result_dict = class_allocation
    return result_str, result_dict
