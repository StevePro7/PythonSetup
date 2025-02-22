import random
import string


def generate_random_string(length):
    """Generate a random string of lowercase letters and digits."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def generate_random_file(filename, num_lines, line_length):
    """Generate a file of random lines with the given number and length."""
    with open(filename, 'w') as f:
        for i in range(num_lines):
            random_line = generate_random_string(line_length) + '\n'
            f.write(random_line)


if __name__ == '__main__':
    # generate 1,000,000 lines of 1000 characters each
    generate_random_file('random.txt', 1_000_000, 1000)
