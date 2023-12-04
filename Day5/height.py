student_heights = input("Enter the height of the students: ").split(" ")

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


total_height = 0

for height in student_heights:
    total_height += height


total_students = len(student_heights)
average_weight = total_height / total_students

print(f"The total height of the students is: {total_height}")
print(f"The total number of students is: {total_students}")
print(f"The average height of the students is {average_weight}")