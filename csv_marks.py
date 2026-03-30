import csv


with open('marks.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'subject', 'marks'])
    writer.writeheader()
    writer.writerow({'name': 'bhavani', 'subject': 'Math', 'marks': 85})
    writer.writerow({'name': 'ram', 'subject': 'Science', 'marks': 65})
    writer.writerow({'name': 'siva', 'subject': 'English', 'marks': 90})


passed_students = []
with open('marks.csv', mode='r') as file:
    reader = csv.DictReader(file)
    print("Students scoring more than 70:")
    for row in reader:
        if int(row['marks']) > 70:
            print(f"{row['name']} scored {row['marks']} in {row['subject']}")
            passed_students.append(row)


with open('passed.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'subject', 'marks'])
    writer.writeheader()
    for student in passed_students:
        writer.writerow(student)