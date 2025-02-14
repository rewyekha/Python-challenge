import pandas as pd
import re
from collections import Counter

def extract_group_counts(file_path, sheet_name="Input Data sheet", column_name="Additional comments"):
    """
    Extracts and counts occurrences of unique group names from an Excel sheet.
    :param file_path: Path to the Excel file.
    :param sheet_name: Name of the sheet containing data.
    :param column_name: Name of the column to search for group names.
    :return: A DataFrame with group names and their occurrence counts.
    """
    # Load the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Counter for group occurrences
    group_counter = Counter()
    
    for comment in df[column_name].dropna():
        # Find all occurrences of group names
        matches = re.findall(r"(?:Groups|Group Names) : \[code\]<I>(.*?)</I>\[/code\]", str(comment))

        for match in matches:
            groups = [group.strip() for group in match.split(",")]
            group_counter.update(groups)

    # Convert to DataFrame for structured output
    result_df = pd.DataFrame(group_counter.items(), columns=["Group name", "Number of occurrences"])

    return result_df

# File path (update if needed)
file_path = "coding challenge test.xlsx"  

# Run the function and save output
group_counts_df = extract_group_counts(file_path)
print(group_counts_df)

# Save to a new Excel file
group_counts_df.to_excel("group_counts_output.xlsx", index=False)
print("\n✅ Output saved as 'group_counts_output.xlsx'")
