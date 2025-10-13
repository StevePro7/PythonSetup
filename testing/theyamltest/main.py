inName = "inHelloWorld.yaml"
outName = "outHelloWorld.yaml"

def prepend_non_empty_lines(inName, outName):
    with open(inName, 'r', encoding='utf-8') as inFile:
        lines = inFile.readlines()

    modified_lines = []
    for line in lines:
        if line.strip():  # If the line is not empty or whitespace
            modified_lines.append(f'&nbsp;&nbsp;{line}')
        else:
            modified_lines.append(line)

    with open(outName, 'w', encoding='utf-8') as outFile:
        outFile.writelines(modified_lines)


# Example usage
#yaml_file = 'hello-world.yml'
prepend_non_empty_lines(inName, outName)
