Work 01

Check for NULLs
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

No. pregnancies OK to be zero
but features that don't make sense to be zero:
    "Glucose": 5,
    "BloodPressure": 35,
    "SkinThickness": 227,
    "Insulin": 374,
    "BMI": 11,


CORRELATIONS
Glucose         Insulin         0.58
Age             Pregnancies     0.54
Glucose         Outcome         0.49
SkinThickness   BMI             0.65

Negative correlation
DiabetesPedigreeFunction    Pregnancies     -0.034

Multicollinearity
In general a correlatio coefficient of >0.7 among two
features indicates the presence of multicollinearity
hence our data is free from multicollinearity!


Group features by the Outcome
Line plot
the mean value of each feature is more for diabetic women than non-diabetic women

Box plots
highlight outliers

For completeness check count plot the Outcome
The dataset is not imbalanced


Univeriate plot
Normal      BloodPressure, SkinThickness, BMI
Skewed      other features

Replace normal distributions with   mean
Replace skewed distributions with   median


Outliers
We see outliers for every feature
therefore we have to remove / replace outliers to get better accuracy

