from pathlib import Path

# Source template file
template_file = "../Managers/BaseManager.py"

# List of manager names
managers = []

with open("../Files/managers.txt", "r") as file:
    managers = [line.strip() for line in file if line.strip()]

# Read the template content
template_text = Path(template_file).read_text()

# Create each manager file
for manager in managers:
    if manager.startswith("#"):
        continue

    new_text = template_text.replace("BaseManager", manager)

    output_file = f"../Managers/{manager}.py"
    Path(output_file).write_text(new_text)

    print(f"Created: {output_file}")