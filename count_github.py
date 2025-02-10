import pandas as pd
import os
import time

# Load the CSV files
files = ["questions.csv", "question_tags.csv"]  # Replace with actual file names
count = 0
chunk_size = 100000

# Track processing time
start_time = time.time()
processed_files = 0
total_files = len(files)

for file in files:
    print(f"⏳ Processing file {processed_files + 1}/{total_files}: {file} ...")
    file_count = 0

    try:
        for chunk_index, chunk in enumerate(pd.read_csv(file, encoding='utf-8', on_bad_lines='skip', chunksize=chunk_size)):
            chunk_count = chunk.apply(lambda row: row.astype(str).str.contains("GitHub", case=False).any(), axis=1).sum()
            file_count += chunk_count
            print(f"   ✅ Processed chunk {chunk_index + 1}, found {chunk_count} matches.")

    except Exception as e:
        print(f"⚠️ Error processing {file}: {e}")

    print(f"📊 {file}: {file_count} total matches found.")
    count += file_count
    processed_files += 1

    # Estimate remaining time
    elapsed_time = time.time() - start_time
    avg_time_per_file = elapsed_time / processed_files
    remaining_time = avg_time_per_file * (total_files - processed_files)
    print(f"⏳ Estimated remaining time: {remaining_time:.2f} seconds\n")

# Print and save the final result
print(f"🎉 Done! Total lines containing 'GitHub': {count}")
output_dir = "_output"
os.makedirs(output_dir, exist_ok=True)
with open(f"{output_dir}/count_github.txt", "w") as f:
    f.write(f"Total lines containing 'GitHub': {count}\n")
