Compo Entry
16-Nov-2024

CompoEntry
~/GitHub/StevePro/PythonSetup/Kaggle

Interpreter type:	Base conda
Path to conda		~/miniconda3/bin/conda

source ~/miniconda3/bin/activate


FINDINGS
<br />
Check for NULLs
```
{
    "Pregnancies": 111,
    "Glucose": 5,
    "BloodPressure": 35,
    "SkinThickness": 227,
    "Insulin": 374,
    "BMI": 11,
    "DiabetesPedigreeFunction": 0,
    "Age": 0,
    "Outcome": 500
}
```
No. pregnancies OK to be zero but features that don't make sense to be zero:
```
    "Glucose": 5,
    "BloodPressure": 35,
    "SkinThickness": 227,
    "Insulin": 374,
    "BMI": 11,
```
CORRELATIONS
```
Glucose         Insulin         0.58
Age             Pregnancies     0.54
Glucose         Outcome         0.49
SkinThickness   BMI             0.65
```
Negative correlation
```
DiabetesPedigreeFunction    Pregnancies     -0.034
```
Multicollinearity
<br />
In general a correlatio coefficient of >0.7 among two
features indicates the presence of multicollinearity
hence our data is free from multicollinearity!

Outliers
<br />
We see outliers for every feature therefore we have to remove / replace outliers to get better accuracy

Classification Report 
```
              precision    recall  f1-score   support

           0       0.84      0.90      0.87        80
           1       0.76      0.64      0.69        39

    accuracy                           0.82       119
   macro avg       0.80      0.77      0.78       119
weighted avg       0.81      0.82      0.81       119
```
Confusion Matrix
```
TN TP       True  Neg   True  Pos
FN FP       False Neg   False Pos
[[72  8]
 [14 25]]
 
TN          True  Neg   72
TP          True  Pos    8
FN          False Neg   14
FP          False Pos   25
```