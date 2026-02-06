import csv

def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            student_reports = []
            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                average = round((math + science + english) / 3, 2)
                status = "Pass" if average >= 60 else "Fail"

                student_reports.append({
                    'Name': name,
                    'Math': math,
                    'Science': science,
                    'English': english,
                    'Average': average,
                    'Status': status
                })
    
        with open(output_file, 'w', newline='') as file:
            fieldnames = ['Name', 'Math', 'Science', 'English', 'Average', 'Status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)
        
        print(f"Student report generated in: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except KeyError:
        print(f"Invalid column name in the input file")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = 'students.csv'
output_file = "student_report.csv"

process_student_data(input_file, output_file)