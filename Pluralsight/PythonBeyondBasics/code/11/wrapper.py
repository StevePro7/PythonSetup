def wrap(text: str, line_length: int) -> str:
    # DO NOT DO THIS - THIS IS BAD
    # assert line_length > 0, "line_length must be positive"
    # rather do this
    if line_length < 1:
        raise ValueError(f"line_length {line_length} is not positive")

    words: list[str] = text.split()

    # Also, ensure that line_length <= the longest word in the text
    longest_word: int = max(map(len, words))
    if longest_word > line_length:
        raise ValueError(f"line_length must be at least as long as the longest word: {longest_word}")

    lines_of_words = list()
    current_line_length = line_length
    for word in words:
        if current_line_length + len(word) > line_length:
            lines_of_words.append(list())
            current_line_length = 0

        lines_of_words[-1].append(word)
        current_line_length += len(word) + len(' ')

    lines = [' '.join(line_of_words) for line_of_words in lines_of_words]
    result = '\n'.join(lines)
    assert all(len(line) <= line_length for line in result.splitlines())
    return result


def main():
    text: str = "The Sega Master System (SMS)[c] is a third-generation 8-bit home video game console manufactured by Sega. It was originally a remodeled export version of the Sega Mark III, the third iteration of the SG-1000 series of consoles, which was released in Japan in 1985 and featured enhanced graphical capabilities over its predecessors. The Master System launched in North America in 1986, followed by Europe in 1987, and Brazil in 1989. A Japanese version of the Master System was also launched in 1987, which features a few enhancements over the export models (and by proxy the original Mark III): a built-in FM audio chip, a rapid-fire switch, and a dedicated port for the 3D glasses. A cost-reduced model known as the Master System II was released in 1990 in North America and Europe."
    print(text)

    result: str = wrap(text, 20)
    print(result)


if __name__ == '__main__':
    main()
