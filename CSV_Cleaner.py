import csv
import re

# File paths (update if needed)
input_file = r"C:\Users\Kai\Documents\RAW.csv"
output_file = r"C:\Users\Kai\Documents\CLEANED.csv"

# Function to clean unwanted characters and fix line endings
def clean_text(text):
    if text is None:
        return ""
    
    # Remove non-printable characters (including \377, other control chars)
    cleaned = re.sub(r'[^\x20-\x7E]', '', text)  
    
    # Ensure Unix-style line endings
    cleaned = cleaned.replace('\r', '')  # Remove all carriage returns (^M)
    
    return cleaned.strip()

# Open and clean the CSV, enforcing Unix line endings
with open(input_file, "r", newline="", encoding="utf-8", errors="ignore") as infile, \
     open(output_file, "w", newline="\n", encoding="utf-8") as outfile:  # Enforce Unix LF endings

    reader = csv.reader(infile)
    writer = csv.writer(outfile, lineterminator="\n")  # Enforce Unix line endings

    for row in reader:
        cleaned_row = [clean_text(cell) for cell in row]  # Clean each cell
        writer.writerow(cleaned_row)

print(f"CSV cleaned successfully! Saved as: {output_file} (with Unix line endings)")

