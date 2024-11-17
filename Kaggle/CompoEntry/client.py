from server import Server

def main():
    filepath: str = "data.csv"
    print(filepath)

    server: Server = Server()
    server.read_csv(filepath)
    server.extract_headers()
    #server.head(5)
    #server.shape()
    server.check_for_nulls()
    server.replace_zeros()
    #server.describe()
    #server.missing_numbers()
    #server.correlation_matrix()          # heatmap
    #server.groupby_outcome_line()
    #server.groupby_outcome_bars()
    #server.groupby_outcome_boxs()
    #server.count_plot()                   # Outcome balanced?
    #server.univariate_plotting()
    server.replace_distributions()
    #TODO - Imputer
    #server.check_for_outliers()
    server.detect_outliers()

    #server.check_for_outliers()          # outliers removed
    #server.bivariate_plot_01()
    #server.bivariate_plot_02()
    #server.bivariate_plot_03()
    #server.bivariate_plot_04()
    #server.bivariate_plot_05()

    server.dropna()
    server.train_model()
    server.classify_report()
    server.confuse_matrix()
    #server.confuse_matrix_draw()          # heatmap
    server.cross_validate()

    server.roc_curve()
    #server.roc_curve_draw()
    server.auc_curve()

if __name__ == '__main__':
    main()
