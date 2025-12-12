import os
import re

project_root = '.'
output_file = 'unique_imports.txt'

import_pattern = re.compile(r'^\s*(import\s+[^\n]+|from\s+[^\n]+import\s+[^\n]+)', re.MULTILINE)
unique_imports = set()

for dirpath, _, filenames in os.walk(project_root):
    for filename in filenames:
        if filename.endswith('.py'):
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for match in import_pattern.findall(content):
                    unique_imports.add(match.strip())
                    
# Categorize imports
third_party = []
project_relative = []

for imp in unique_imports:
    # Check if it's a relative import (starts with 'from .'
    if imp.startswith('from .'):
        project_relative.append(imp)
    else:
        third_party.append(imp)
        
# Write to output file with categories
with open(output_file, 'w', encoding='utf-8') as out:
    out.write('=' * 60 + '\n')
    out.write('THIRD PARTY PACAKGES\n')
    out.write('=' * 60 + '\n')
    for imp in sorted(third_party, key=str.lower):
        out.write(imp + '\n')

    out.write('=' * 60 + '\n')
    out.write('PROJECT-RELATIVE IMPORTS\n')
    out.write('=' * 60 + '\n')
    for imp in sorted(project_relative, key=str.lower):
        out.write(imp + '\n')

print(f'Unique imports written to {output_file} (categorized and sorted)')