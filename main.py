def calculate_marks(marks):
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    print("Marks:", marks)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Average Marks:", average)

marks = [85, 92, 78, 88, 95]

calculate_marks(marks)