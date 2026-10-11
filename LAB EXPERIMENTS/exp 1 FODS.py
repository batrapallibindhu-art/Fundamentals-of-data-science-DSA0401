
import numpy as np

# Store marks of 4 students in 4 subjects
student_scores = np.array([
    [85, 78, 92, 70],
    [90, 88, 85, 80],
    [75, 95, 89, 85],
    [80, 85, 94, 75]
])

# Subject names
subjects = ["Math", "Science", "English", "History"]

# Calculate average marks of each subject
average_scores = np.mean(student_scores, axis=0)

# Find the subject with the highest average
highest_index = np.argmax(average_scores)

# Display average marks
print("Average marks of each subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", average_scores[i])

print("Subject with highest average:",
      subjects[highest_index])
print("Highest average marks:", average_scores[highest_index])
