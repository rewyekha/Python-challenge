# DigitalXC Coding Challenge Test

## Author
Challenge completed by **Reyas Khan**  
[LinkedIn](https://www.linkedin.com/in/reyas-khan-16640825b/) | [Portfolio](https://rewyekha.github.io/#/home)

## Python Coding Challenge Test

### Introduction
Thank you for applying for the role of Automation Specialist at DigitalXC. This challenge evaluates your ability to process and extract meaningful insights from structured data using Python.

### Problem Statement
You will write a Python program to:
- Read data from the provided CSV file ("Input-Data.csv").
- Browse through all rows under the "Additional Comments" column.
- Identify lines containing **Groups: [code]<I>XXXX</I>[/code]**.
- Extract and list all unique groups found in the dataset.
- Count the number of occurrences of each unique group and present them in a tabular format.

### Expected Output Format
| Group Name | Number of Occurrences |
|------------|----------------------|
| Huntingdon and Liz areas | 2 |
| SML Group GMs | 1 |
| Eastend GMs | 3 |

### Code Logic and Flow

1. **Read the CSV File:**
   - Open and read the "Input-Data.csv" file using the `csv` module.
   - Store relevant data from the "Additional Comments" column.

2. **Extract Group Information:**
   - Use regular expressions (`re` module) to detect patterns matching **Groups: [code]<I>XXXX</I>[/code]**.
   - Extract the group names from the matched text.

3. **Process Data and Count Unique Groups:**
   - Store extracted group names in a dictionary where the key is the group name and the value is its count.
   - Ensure multiple groups in a single entry are split properly and counted separately.

4. **Output the Results:**
   - Save the results into a new CSV file with columns `Group Name` and `Number of Occurrences`.
   - Display the output in a structured format.

### Functions Breakdown

#### `parse_csv(file_path: str) -> list`
Reads and extracts text from the "Additional Comments" column.

#### `extract_groups(text: str) -> list`
Uses regular expressions to identify and extract groups from the given text.

#### `count_groups(group_list: list) -> dict`
Aggregates the extracted group names and counts their occurrences.

#### `save_to_csv(output_file: str, data: dict)`
Writes the final grouped data into a new CSV file.

### Installation & Usage

#### Clone the Repository
```sh
git clone <repository_url>
cd <repository_directory>
```

#### Run the Script
```sh
python extract_groups.py
```

#### Dependencies
- Python 3.x
- `csv` module (built-in)
- `re` module (built-in)

---

## Full Stack Engineer Coding Challenge

### Secret Santa Game

#### Background
Acme Inc. is organizing a **Secret Santa** event among employees. Each employee must be randomly assigned a recipient ("Secret Child") while ensuring fairness and avoiding conflicts from previous years.

### Problem Statement
Your task is to automate the Secret Santa assignment process using Python. The program should:
1. Read employee details from a CSV file.
2. Assign each employee a unique Secret Child while following these rules:
   - An employee cannot be assigned themselves.
   - Employees should not receive the same Secret Child as last year.
   - Each employee must have exactly one Secret Child.
   - Each Secret Child should be assigned only once.
3. Generate a new CSV file containing the Secret Santa pairings.
4. Handle edge cases, errors, and ensure the program is modular and scalable.

### Expected Output Format
A new CSV file with:
| Employee Name | Employee Email | Secret Child Name | Secret Child Email |
|--------------|--------------|------------------|------------------|

### Code Logic and Flow

1. **Read Employee Data:**
   - Parse the employee list from the CSV file.
   - Store employees in a list of objects.

2. **Ensure Unique Assignments:**
   - Load last year's assignments (if available) and store them in a dictionary.
   - Check for duplicates or invalid assignments and reassign as necessary.

3. **Randomized Assignment Using OOP:**
   - Implement object-oriented design using an `Employee` class and a `SecretSanta` class.
   - Randomly shuffle employees and assign Secret Children ensuring all constraints are met.
   - If a valid assignment isn't possible, retry until a valid set is found.

4. **Save Output:**
   - Write the final Secret Santa assignments into a CSV file.

### Object-Oriented Design & Functions Breakdown

#### `class Employee`
Represents an employee with attributes:
- `name` (str)
- `email` (str)
- `previous_child` (str, optional)

#### `class SecretSanta`
Handles Secret Santa logic:
- Reads and processes employee data.
- Assigns Secret Children following constraints.
- Saves results to a CSV file.

##### `assign_secret_santa(self)`
Randomly assigns Secret Santa pairings while ensuring constraints are met.

##### `load_previous_assignments(self, file_path: str) -> dict`
Loads last year's assignments to prevent duplicate pairings.

##### `save_assignments(self, output_file: str)`
Writes the final Secret Santa pairings to a CSV file.

### Installation & Usage

#### Clone the Repository
```sh
git clone <repository_url>
cd <repository_directory>
```

#### Run the Script
```sh
python secret_santa.py
```

#### Dependencies
- Python 3.x
- `csv` module (built-in)
- `random` module (built-in)

### Solution Expectations

- **Modularity & Extensibility:**
  - Uses OOP principles for better maintainability.
  - Functions are independent and reusable.
- **Error Handling:**
  - Handles invalid inputs and file errors.
- **Testing:**
  - Includes unit tests for core functions.
- **Tools:**
  - Use GitHub codespace for submission.

---




