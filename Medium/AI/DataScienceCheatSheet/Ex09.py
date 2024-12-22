# 9. Regular Expressions
import re

# Match Pattern
pattern = r"\d+"
result = re.findall(pattern, "123 Main Street")

# Replace Pattern
new_text = re.sub(r"\d+", "#", "123 Main Street")