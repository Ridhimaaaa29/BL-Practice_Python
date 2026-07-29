"""
PROG 1: School Result
School Result: Refactor the use case to use a dictionary. Use cases are listed:

=> Create sample 20 student names in a list \

=> For each student, create a dictionary having the key as name,Value as another dictionary with keys as Gender, Physics Marks, Chemistry Marks , Maths Marks and Number of Days attended in the last 120 days. \

=> Full marks for each subject is 50. Fill this data by randomly generating data for each student.

Note : Marks should be between 0.0 to 50.0 and attendance should be between 1 to 120.
Gender can be ‘M’ or ‘F’.  Plan using random.choice() for this.
=> Compute total marks obtained, % marks, % attendance and grade for each student. \

=> Following table shows % marks obtained and corresponding grade table

% Marks       Grade
Above 90%       A+
80% - 90%       A
60% - 80%       B
50-60 %         C
30-50%          D
Less than 30%   F

=> Modify the earlier dictionary to accommodate these new keys and respective values. \

=> Based on user choice show the result of a student either garde wise or percentage wise.

=> If the overall grade is F or if the total % is less than 30%, please keep a remark at the bottom : Failed, work hard to do better next time.
Alternatively, a message comes - Congratulations!, Passed Successfully.

Summary generation: Plan generating following summary

=> Overall Pass %
=> Overall Grade Wise percentage distribution
=> Name of the student who topped
=> Names of students who topped subject wise
=> List of students who passed - names with alphabetically sorted manner and their corresponding full marks % and overall grade.
=> List of students who passed, sorted based on total marks \

Hint => 1.Plan using built in functionsorted() 2.Organize your code in appropriate modules/ functions

Note => Try with different inputs


TESTCASE 1:

Input =>
Enter 'grade' to display results by grade or 'percentage' to display results by percentage: percentage

Output => \

Name: Student1
Gender: F
Marks:
- Physics: 23.2
- Chemistry: 16.3
- Maths: 2.2
Attendance: 10
Total Marks: 41.7/150
Percentage Marks: 27.8%
Attendance: 10
Grade: F
Remarks: Failed, work hard to do better next time
Note =>
=> Everytime you execute the code , the output will differ.
=> Output is very lengthy So didn't paste the whole output
"""

# write your code here  
import random

def generate_student_data(student_names):
    """
    Generates random marks, gender, and attendance for each student.
    """
    students_data = {}
    for name in student_names:
        students_data[name] = {
            'Gender': random.choice(['M', 'F']),
            'Physics Marks': round(random.uniform(0.0, 50.0), 1),
            'Chemistry Marks': round(random.uniform(0.0, 50.0), 1),
            'Maths Marks': round(random.uniform(0.0, 50.0), 1),
            'Number of Days attended': random.randint(1, 120)
        }
    return students_data

def assign_grade(percentage):
    """
    Returns grade based on percentage.
    """
    if percentage > 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 30:
        return 'D'
    else:
        return 'F'

def compute_results(students_data):
    """
    Computes total marks, percentages, grade, and remarks for each student.
    Modifies the dictionary in place.
    """
    for name, data in students_data.items():
        total_marks = data['Physics Marks'] + data['Chemistry Marks'] + data['Maths Marks']
        percentage_marks = round((total_marks / 150.0) * 100, 2)
        percentage_attendance = round((data['Number of Days attended'] / 120.0) * 100, 2)
        grade = assign_grade(percentage_marks)
        
        if grade == 'F' or percentage_marks < 30.0:
            remarks = "Failed, work hard to do better next time"
        else:
            remarks = "Congratulations!, Passed Successfully"

        # Update dictionary with computed metrics
        data['Total Marks'] = total_marks
        data['Percentage Marks'] = percentage_marks
        data['Percentage Attendance'] = percentage_attendance
        data['Grade'] = grade
        data['Remarks'] = remarks

def display_student_results(students_data, choice):
    """
    Displays results of students based on user choice ('grade' or 'percentage').
    """
    print("-" * 50)
    for name, data in students_data.items():
        print(f"Name: {name}")
        print(f"Gender: {data['Gender']}")
        print("Marks:")
        print(f"- Physics: {data['Physics Marks']}")
        print(f"- Chemistry: {data['Chemistry Marks']}")
        print(f"- Maths: {data['Maths Marks']}")
        print(f"Attendance: {data['Number of Days attended']}")
        print(f"Total Marks: {data['Total Marks']}/150")
        print(f"Percentage Marks: {data['Percentage Marks']}%")
        print(f"Attendance: {data['Number of Days attended']}")
        print(f"Grade: {data['Grade']}")
        print(f"Remarks: {data['Remarks']}")
        print("-" * 50)

def generate_summary(students_data):
    """
    Generates overall summary including pass percentage, grade distribution,
    toppers, and sorted lists of passed students.
    """
    total_students = len(students_data)
    passed_students = [name for name, data in students_data.items() if data['Grade'] != 'F']
    overall_pass_percentage = (len(passed_students) / total_students) * 100

    # Grade distribution
    grades = ['A+', 'A', 'B', 'C', 'D', 'F']
    grade_counts = {g: 0 for g in grades}
    for data in students_data.values():
        grade_counts[data['Grade']] += 1

    # Toppers
    overall_topper = max(students_data.keys(), key=lambda k: students_data[k]['Total Marks'])
    physics_topper = max(students_data.keys(), key=lambda k: students_data[k]['Physics Marks'])
    chemistry_topper = max(students_data.keys(), key=lambda k: students_data[k]['Chemistry Marks'])
    maths_topper = max(students_data.keys(), key=lambda k: students_data[k]['Maths Marks'])

    # Passed students list sorted alphabetically
    passed_alphabetical = sorted(passed_students)

    # Passed students list sorted by total marks (descending)
    passed_by_marks = sorted(passed_students, key=lambda k: students_data[k]['Total Marks'], reverse=True)

    # Display Summary
    print("\nSummary:")
    print(f"Overall Pass Percentage: {overall_pass_percentage:.1f}%")
    print("Grade-wise Percentage Distribution:")
    for g in ['A+', 'A', 'B', 'C', 'D']:
        dist = (grade_counts[g] / total_students) * 100
        print(f"- Grade {g}: {dist:.1f}%")

    print(f"Top Student: {overall_topper}")
    print("Top Students Subject-wise:")
    print(f"- Physics: {physics_topper}")
    print(f"- Chemistry: {chemistry_topper}")
    print(f"- Maths: {maths_topper}")

    print("List of Students Who Passed (Alphabetically sorted):")
    for name in passed_alphabetical:
        p_data = students_data[name]
        print(f"- {name}: {p_data['Percentage Marks']}% ({p_data['Grade']})")

    print("List of Students Who Passed (Sorted based on Total Marks):")
    for name in passed_by_marks:
        p_data = students_data[name]
        print(f"- {name}: {p_data['Total Marks']}/150 ({p_data['Percentage Marks']}%, {p_data['Grade']})")

def main():
    # Step 1: Create sample 20 student names
    student_names = [f"Student{i}" for i in range(1, 21)]

    # Step 2 & 3: Generate student data
    students_data = generate_student_data(student_names)

    # Step 4 & 5: Compute total, percentages, grades, and remarks
    compute_results(students_data)

    # Step 6: Get user choice
    choice = input("Enter 'grade' to display results by grade or 'percentage' to display results by percentage: ").strip().lower()

    # Display Student Results
    display_student_results(students_data, choice)

    # Step 7: Summary generation
    generate_summary(students_data)

if __name__ == "__main__":
    main()
