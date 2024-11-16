from Steps.step01 import Step01

def work():
    filepath: str = "../data.csv"

    step: Step01 = Step01()
    step.read_csv(filepath)
    step.extract_headers()
    #step.head(5)
    #step.shape()
    step.check_for_nulls()
    step.replace_zeros()
    #step.describe()
    #step.missing_numbers()
    #step.correlation_matrix()          # heatmap
    #step.groupby_outcome_line()
    step.groupby_outcome_bars()

if __name__ == '__main__':
    work()