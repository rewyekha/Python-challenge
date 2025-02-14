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
        """
        Assigns each employee a unique secret child using random shuffling.
        :return: A dictionary mapping giver emails to their assigned secret child.
        """
        # Create a shuffled copy of the employee list
        participants = self.employees[:]
        random.shuffle(participants)
        
        assignments = {}

        # Assign each employee a secret child
        for i in range(len(participants)):
            giver = participants[i]
            receiver = participants[(i + 1) % len(participants)]  # Circular assignment
            assignments[giver.email] = receiver
        
        return assignments

def parse_input_data(data: str) -> List[Employee]:
    """
    Parses input employee data from a multi-line string.
    :param data: Input string containing employee names and emails.
    :return: A list of Employee objects.
    :raises ValueError: If the input format is incorrect (e.g., missing emails).
    """
    lines = [line.strip() for line in data.strip().split("\n") if line.strip()]
    
    if len(lines) % 2 != 0:
        raise ValueError("Invalid input format: Missing email for an employee.")
    
    employees = []

    # Iterate over lines in pairs (name, email)
    for i in range(1, len(lines), 2):  
        name = lines[i - 1] 
        email = lines[i]  
        employees.append(Employee(name, email))
    
    return employees

def write_output(filepath: str, assignments: Dict[str, Employee]):
    """
    Writes the Secret Santa assignments to a CSV file.
    :param filepath: Path to the output CSV file.
    :param assignments: Dictionary of Secret Santa pairs (giver email -> secret child).
    """
    with open(filepath, 'w', newline='') as csvfile:
        fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()

        # Write each Secret Santa assignment to the file
        for giver_email, receiver in assignments.items():
            writer.writerow({
                'Employee_Name': receiver.name,
                'Employee_EmailID': giver_email,
                'Secret_Child_Name': receiver.name,
                'Secret_Child_EmailID': receiver.email
            })

if __name__ == "__main__":
    input_data = """Employee_Name\nEmployee_EmailID\nHamish Murray\nhamish.murray@acme.com\nLayla Graham\nlayla.graham@acme.com\nMatthew King\nmatthew.king@acme.com\nBenjamin Collins\nbenjamin.collins@acme.com\nIsabella Scott\nisabella.scott@acme.com\nCharlie Ross\ncharlie.ross@acme.com\nHamish Murray\nhamish.murray.sr@acme.com\nPiper Stewart\npiper.stewart@acme.com\nSpencer Allen\nspencer.allen@acme.com\nCharlie Wright\ncharlie.wright@acme.com\nHamish Murray\nhamish.murray.jr@acme.com\nCharlie Ross\ncharlie.ross.jr@acme.com\nEthan Murray\nethan.murray@acme.com\nMatthew King\nmatthew.king.jr@acme.com\nMark Lawrence\nmark.lawrence@acme.com"""

    # Parse input and assign Secret Santa pairs
    employees = parse_input_data(input_data)
    assigner = SecretSantaAssigner(employees)
    new_assignments = assigner.assign_secret_santa()

    # Write output to CSV file
    write_output("secret_santa_assignments.csv", new_assignments)
    print("✅ Secret Santa assignments successfully generated!")
