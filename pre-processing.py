from glob import glob
from tqdm import tqdm
# Search folders and subfolders of content for markdown files
files = glob('content/**/*.md', recursive=True)

# Get producer files
producer_files = [f for f in files if f.startswith('content/producers')]

# Build a mapping from original links to corrected links
producer_mapping = {}
for producer_file in producer_files:
    producer = producer_file.split('/')[-1].split('.md')[0]
    producer_link = f"[[{producer}]]"
    producer_link_fixed = f"[[producers/{producer}]]"
    producer_mapping[producer_link] = producer_link_fixed

# Process each file once
for file in tqdm(files):
    with open(file, 'r') as f:
        filedata = f.read()
    newdata = filedata

    # Perform all replacements
    for original_link, corrected_link in producer_mapping.items():
        if original_link in newdata:
            newdata = newdata.replace(original_link, corrected_link)

    # Write back only if changes were made
    if newdata != filedata:
        with open(file, 'w') as f:
            f.write(newdata)

print(len(producer_files))
