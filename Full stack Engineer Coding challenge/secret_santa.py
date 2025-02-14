import csv
import random
from typing import List, Dict

class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"{self.name} ({self.email})"

class SecretSantaAssigner:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    def assign_secret_santa(self) -> Dict[str, Employee]:
        participants = self.employees[:]
        random.shuffle(participants)
        assignments = {}
        
        for i in range(len(participants)):
            giver = participants[i]
            receiver = participants[(i + 1) % len(participants)]
            assignments[giver.email] = receiver
        
        return assignments

def parse_input_data(data: str) -> List[Employee]:
    lines = [line.strip() for line in data.strip().split("\n") if line.strip()]
    if len(lines) % 2 != 0:
        raise ValueError("Invalid input format: Missing email for an employee.")
    employees = []
    for i in range(1, len(lines), 2):  # Skip header
        name = lines[i - 1]
        email = lines[i]
        employees.append(Employee(name, email))
    return employees

def write_output(filepath: str, assignments: Dict[str, Employee]):
    with open(filepath, 'w', newline='') as csvfile:
        fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for giver_email, receiver in assignments.items():
            writer.writerow({'Employee_Name': receiver.name, 'Employee_EmailID': giver_email, 'Secret_Child_Name': receiver.name, 'Secret_Child_EmailID': receiver.email})

if __name__ == "__main__":
    input_data = """Employee_Name\nEmployee_EmailID\nHamish Murray\nhamish.murray@acme.com\nLayla Graham\nlayla.graham@acme.com\nMatthew King\nmatthew.king@acme.com\nBenjamin Collins\nbenjamin.collins@acme.com\nIsabella Scott\nisabella.scott@acme.com\nCharlie Ross\ncharlie.ross@acme.com\nHamish Murray\nhamish.murray.sr@acme.com\nPiper Stewart\npiper.stewart@acme.com\nSpencer Allen\nspencer.allen@acme.com\nCharlie Wright\ncharlie.wright@acme.com\nHamish Murray\nhamish.murray.jr@acme.com\nCharlie Ross\ncharlie.ross.jr@acme.com\nEthan Murray\nethan.murray@acme.com\nMatthew King\nmatthew.king.jr@acme.com\nMark Lawrence\nmark.lawrence@acme.com"""
    employees = parse_input_data(input_data)
    assigner = SecretSantaAssigner(employees)
    new_assignments = assigner.assign_secret_santa()
    write_output("secret_santa_assignments.csv", new_assignments)
    print("Secret Santa assignments successfully generated!")
