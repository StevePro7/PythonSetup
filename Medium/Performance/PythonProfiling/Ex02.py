import re


def baseline():
    num_total_matches = 0
    pattern1 = r"[0-9]{1}bob"
    pattern2 = r"[0-9]{1}rob"

    with open('random.txt', 'rt') as f:
        for line in f:
            line = line.lower()  # make sure our text is all lowercase
            for pattern in [pattern1, pattern2]:
                # Find all occurrences of the pattern in the string
                matches = re.findall(pattern, line)

                # Count the number of matches
                num_matches = len(matches)
                num_total_matches += num_matches

    return num_total_matches
