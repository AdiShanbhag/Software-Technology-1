input_grade: str = input("Enter your grade: ")

if input_grade.isnumeric():
    grade: int = int(input_grade)
    print(grade)
else:
    print("Only numbers allowed")

new_grade: str = input("Enter your grade: ")
if new_grade.replace(".", "", 1).isnumeric():
    grade: float = float(new_grade)
    print(grade)
else:
    print("Only numbers allowed")