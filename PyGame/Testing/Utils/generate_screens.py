from pathlib import Path

# Source template file
template_file = "../Managers/FooManager.py"

# List of manager names
screens = [
    "DiffScreen",
    "ExitScreen",
    "InitScreen",
    "LongScreen",
    "OverScreen",
    "PlayScreen",
    "QuizScreen",
    "ReadyScreen",
    "ScoreScreen",
    "SplashScreen",
    "TestScreen",
    "TitleScreen",
]

# Read the template content
template_text = Path(template_file).read_text()

# Create each manager file
for manager in managers:
    new_text = template_text.replace("FooManager", manager)

    output_file = f"../Managers/{manager}.py"
    Path(output_file).write_text(new_text)

    print(f"Created: {output_file}")