"""Reorder the API Endpoints table in README.md to match ordering.txt."""

import os
import re

root = os.path.join(os.path.dirname(__file__), "..")
ordering_path = os.path.join(root, "ordering.txt")
readme_path = os.path.join(root, "README.md")

# Read ordering.txt to get priority list
with open(ordering_path) as f:
    ordered_paths = [line.strip() for line in f if line.strip()]

priority = {path: i for i, path in enumerate(ordered_paths)}

# Read README.md
with open(readme_path) as f:
    readme = f.read()

# Find the API endpoints table section
start_marker = "## Documentation for API Endpoints"
end_marker = "## Documentation For Models"

start_idx = readme.index(start_marker)
end_idx = readme.index(end_marker)

before = readme[:start_idx]
section = readme[start_idx:end_idx]
after = readme[end_idx:]

# Split section into lines
lines = section.split("\n")

# Separate header lines (title, blank, column headers, separator) from data rows
header_lines = []
data_rows = []
in_data = False

for line in lines:
    if not in_data:
        header_lines.append(line)
        # After the separator line (---), data rows begin
        if re.match(r"^-+\s*\|", line):
            in_data = True
    else:
        if line.strip():
            data_rows.append(line)
        # preserve trailing blank lines as part of the section end

# Extract path from each row: look for **GET** /path pattern
def extract_path(row):
    match = re.search(r"\*\*GET\*\*\s+(/\S+)", row)
    if match:
        # Strip leading / and any trailing whitespace/pipe
        return match.group(1).lstrip("/").rstrip()
    return None

# Sort rows by priority
def sort_key(row):
    path = extract_path(row)
    if path and path in priority:
        return (0, priority[path])
    # Not in ordering.txt: put at end, sorted alphabetically by path
    return (1, path or "")

data_rows.sort(key=sort_key)

# Reconstruct the section
new_section = "\n".join(header_lines) + "\n" + "\n".join(data_rows) + "\n\n"

# Write back
with open(readme_path, "w") as f:
    f.write(before + new_section + after)

print(f"Reordered {len(data_rows)} endpoint rows in README.md")
