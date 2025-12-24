Bias, Variance, and the Trade-Off
14-Dec-2025

https://medium.com/@kiranvutukuri/8-bias-variance-and-the-trade-off-647a7c1f1295
uv init --python 3.11.11
uv venv --python 3.11.11

source ./venv/bin/activate
OR
.venv\Scripts\activate

uv add numpy
uv add matplotlib
uv add scikit-learn


ML
build models that generalize well

bias, variance and trade-offs
underfit, overfit, perform optimally


Underfit    High bias
Overfit     High variance
Balanced    Good fit


BIAS
error introduced by approximating real-world problem with simplified model

high bias       model too simple to capture underlying patterns
Underfitting    model performs poorly on training and test data


VARIANCE
error caused by model being too sensitive to training data

high variance   model memorizes training data including noise
Overfitting     model performs well on training data but poor on test data


TRADE-OFF
bias-variance trade-off = balance btwn model simplicity [BIAS] and complexity [VARIANCE]


CONCLUSION
Underfitting    high bias       low variance    increase model complexity or features
Overfitting     high variance   low bias        simplify model regularize or gather more data