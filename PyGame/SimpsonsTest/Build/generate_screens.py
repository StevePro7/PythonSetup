from pathlib import Path
import textwrap

template_file = "../Game/Screens/BaseScreen.py"

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

template_text = Path(template_file).read_text()

# Normalize template indentation first (VERY important)
template_text = textwrap.dedent(template_text)

for screen in screens:
    new_text = template_text

    # 1. Replace import
    new_text = new_text.replace(
        "from abc import ABC, abstractmethod",
        "from Screens.BaseScreen import BaseScreen"
    )

    # 2. Remove abstract decorator
    new_text = new_text.replace("@abstractmethod", "")

    # 3. Replace base class definition with child class
    new_text = new_text.replace(
        "class BaseScreen(ABC):",
        f"class {screen}(BaseScreen):"
    )

    # 4. Final cleanup (removes accidental indentation drift)
    new_text = textwrap.dedent(new_text).rstrip() + "\n"

    output_file = f"../Game/Screens/{screen}.py"
    Path(output_file).write_text(new_text)

    print(f"Created: {output_file}")