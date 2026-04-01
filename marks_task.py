import csv

# Step 1: Create and write to marks.csv
with open("marks.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    # Columns
    writer.writerow(["name", "subject", "marks"])
    
    # Data (at least 20 rows)
    writer.writerow(["bhavani", "Math", 85])
    writer.writerow(["ram", "Science", 65])
    writer.writerow(["sitha", "English", 35])
    writer.writerow(["siva", "telugu", 15])
    writer.writerow(["parvathi", "chemistry", 25])
    writer.writerow(["krishna", "Evs", 70])
    writer.writerow(["radha", "Gk", 55])
    writer.writerow(["lakshman", "biology", 95])
    writer.writerow(["ravana", "algebra", 76])
    writer.writerow(["hanuman", "statistics", 79])
    writer.writerow(["happy", "physics", 73])
    writer.writerow(["pinky", "astronomy", 71])
    writer.writerow(["smily", "environmental science", 85])
    writer.writerow(["rakesh", "geology", 100])
    writer.writerow(["bhavya", "geography", 52])
    writer.writerow(["kusuma", "economics", 28])
    writer.writerow(["sarvani", "sociology", 70])
    writer.writerow(["devanshi", "history", 65])
    writer.writerow(["sai", "psychology", 95])
    writer.writerow(["sai sri", "political sciences", 54])
   
# Step 2: Read and filter students > 70
passed_students = []

with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if int(row["marks"]) > 70:
            print(row)
            passed_students.append(row)

# Step 3: Write passed students to passed.csv
with open("passed.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "subject", "marks"])
    
    writer.writeheader()
    writer.writerows(passed_students)