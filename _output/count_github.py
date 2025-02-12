import pandas as pd

# Load the CSV files
files = [
    "/home/ubuntu/assignment-01-shuyu-pan831/questions.csv",
    "/home/ubuntu/assignment-01-shuyu-pan831/question_tags.csv"
]
  # Replace with actual file names
count = 0

for file in files:
    df = pd.read_csv(file, nrows=1000)
    count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False).any(), axis=1).sum()

print(f"Total lines containing 'GitHub': {count}")
