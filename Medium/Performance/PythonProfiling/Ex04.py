import graphviz


def make_png(input_file_name, output_file_name):
    dot = graphviz.Source.from_file(input_file_name)
    dot.render(outfile=output_file_name)


if __name__ == '__main__':
    make_png('file.dot', 'file.svg')  # also supports .png, .jpg, etc.
