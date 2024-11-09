Example01
09-Nov-2024

New project | Base Conda
Example01
/home/stevepro/miniconda3/bin/conda

source ~/miniconda3/bin/activate
conda list


Install package seaborn


PACKAGES that could require more attention:
pandas                  CSV to dataframe
matplotlib.pyplot       graphs
seaborn                 correlations
sklearn                 model selection + training


WARNINGS
sklearn
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
Please also refer to the documentation for alternative solver options:


REPORT
              precision    recall  f1-score   support

           0       0.81      0.80      0.80        99
           1       0.64      0.65      0.65        55

    accuracy                           0.75       154
   macro avg       0.72      0.73      0.73       154
weighted avg       0.75      0.75      0.75       154
