import re
from tqdm import tqdm


def wasted_efforts():
    num_total_matches = 0
    # We use compiled regular expressions
    pattern1 = re.compile(r"[0-9]{}rob", flags=re.IGNORECASE)
    # We also use case case-insensitivity instead of changing the lines
    pattern2 = re.compile(r"[0-9]{}bob", flags=re.IGNORECASE)

    with open('random.txt', 'rt') as f:
        # We load lines into a chunk and process it in 1 go
        chunk = []
        for line in tqdm(f, total=1_000_000):
            chunk.append(line)

            if len(chunk) == 1000:
                chunk_str = ''.join(chunk)
                for pattern in [pattern1, pattern2]:
                    # Find all occurrences of the pattern in the string
                    matches = re.findall(pattern, chunk_str)

                    # Count the number of matches
                    num_matches = len(matches)
                    num_total_matches += num_matches

                chunk = []

    # But despite our efforts, this code is still as slow as the original
    return num_total_matches


wasted_efforts()
