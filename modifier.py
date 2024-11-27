import os
import re

# Directory containing the data
folder = 'reddit_data_unfiltered'
new_folder = 'reddit_data_cleaned'
os.makedirs(new_folder, exist_ok=True)

# Regex to match URLs
url_pattern = re.compile(r'https?://\S+|www\.\S+')

def clean_text(text):
    # Remove URLs
    text = url_pattern.sub("", text)
    # Remove asterisks
    text = text.replace('*', '')
    return text

# Process each file in the directory
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    if os.path.isfile(file_path) and filename.startswith('reddit_'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Clean the content
        cleaned_content = clean_text(content)
        
        new_file_path = os.path.join(new_folder, filename)
        # Write the cleaned content back to the file
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f'Processed and cleaned {filename}')
