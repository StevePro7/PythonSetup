import re
from tqdm import tqdm


def single_pattern():
    num_total_matches = 0
    pattern = r"[0-9][rb]ob"  # We now have only one search instead of two

    with open('random.txt', 'rt') as f:
        for line in tqdm(f, total=1_000_000):
            line = line.lower()
            # Find all occurrences of the pattern in the string
            matches = re.findall(pattern, line)

            # Count the number of matches
            num_matches = len(matches)
            num_total_matches += num_matches

    return num_total_matches


single_pattern()
