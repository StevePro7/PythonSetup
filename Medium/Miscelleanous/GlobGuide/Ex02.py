# 2. Searching in Subdirectories
import glob

text_files = glob.glob("**/*.txt", recursive=True)
print(text_files)