class Table:

    def __init__(self, header, *data):
        self.header = header
        self.data = data
        assert len(header) == len(data)

    def _column_width(self, i):
        result = max(len(str(x)) for x in self.data[i])
        return max(len(self.header[i]), result)

    def __str__(self):
        col_count = len(self.header)
        col_widths = [self._column_width(i) for i in range(col_count)]
        format_specs = []
        for i in range(col_count):
            format_specs.append(f'{{:{col_widths[i]}}}')

        result = list()
        result.append(
            format_specs[i].format(self.header[i])
            for i in range(col_count)
        )

        result.append(
            ('=' * col_widths[i]
             for i in range(col_count)
             )
        )

        for row in zip(*self.data):
            result.append(
                [format_specs[i].format(row[i])
                 for i in range(col_count)
                 ]
            )

        result = (' '.join(r) for r in result)
        return '\n'.join(result)
