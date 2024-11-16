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
    #step.groupby_outcome_bars()
    #step.groupby_outcome_boxs()
    #step.count_plot()                   # Outcome balanced?
    #step.univariate_plotting()
    step.replace_distributions()
    #TODO - Imputer
    #step.check_for_outliers()
    step.detect_outliers()
    #step.check_for_outliers()          # outliers removed
    #step.bivariate_plot_01()
    #step.bivariate_plot_02()
    #step.bivariate_plot_03()
    #step.bivariate_plot_04()
    step.bivariate_plot_05()

if __name__ == '__main__':
    work()
